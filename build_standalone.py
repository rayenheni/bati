"""Construit une version 100 % autonome du site (un seul fichier HTML).

Usage : python3 build_standalone.py    (nécessite Pillow : pip install Pillow)
Le fichier généré `apercu-autonome.html` contient CSS, JS, polices et images
en data URI : il fonctionne hors ligne, sans serveur, et dans une iframe sandbox.
Après toute modification de index.html / styles.css / rtl.css / i18n.js /
script.js / fonts.css ou des images, relancer ce script.
"""
import base64, io, re, pathlib
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent
OUT = ROOT / 'apercu-autonome.html'
cache = {}


def img_data(path, max_w=1100, quality=68):
    key = (str(path), max_w, quality)
    if key in cache:
        return cache[key]
    im = Image.open(path).convert('RGB')
    if im.width > max_w:
        im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, 'JPEG', quality=quality, optimize=True, progressive=True)
    uri = 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()
    cache[key] = uri
    return uri


def font_data(path):
    p = str(path)
    if p not in cache:
        ext = path.suffix.lstrip('.').lower()
        mime = {'woff2': 'font/woff2', 'woff': 'font/woff', 'ttf': 'font/ttf'}.get(ext, 'application/octet-stream')
        cache[p] = f'data:{mime};base64,' + base64.b64encode(path.read_bytes()).decode()
    return cache[p]


def inline_css_assets(css, base):
    def repl(m):
        raw = m.group(1).strip().strip('"\'')
        if raw.startswith('data:'):
            return m.group(0)
        p = (ROOT / base / raw.split('?')[0].split('#')[0]).resolve()
        if not p.exists():
            print('  !! missing', raw)
            return m.group(0)
        if p.suffix.lower() in ('.woff', '.woff2', '.ttf'):
            uri = font_data(p)
        elif p.suffix.lower() in ('.jpg', '.jpeg', '.png', '.webp'):
            uri = img_data(p)
        else:
            return m.group(0)
        return 'url("' + uri + '")'
    return re.sub(r'url\(([^)]+)\)', repl, css)


html = (ROOT / 'index.html').read_text(encoding='utf-8')

# --- CSS inline, dans l'ordre d'origine ---
css_files = ['fonts/fonts.css', 'styles.css', 'rtl.css']
styles = '\n'.join(
    '/* ===== ' + f + ' ===== */\n' + inline_css_assets((ROOT / f).read_text(encoding='utf-8'), pathlib.Path(f).parent)
    for f in css_files
)
for f in css_files:
    html = re.sub(r'<link\s+rel="stylesheet"\s+href="' + re.escape(f) + r'(?:\?[^\"]*)?"\s*/?>', '', html)
html = re.sub(r'<link\s+rel="preload"[^>]*>\n?', '', html)
html = html.replace('</head>', '<style id="styles-inlines">\n' + styles + '\n</style>\n</head>')

# --- JS inline, dans l'ordre d'origine ---
js = ''
for f in ['i18n.js', 'script.js']:
    html = re.sub(r'<script\s+src="' + re.escape(f) + r'"></script>', '', html)
    js += '/* ===== ' + f + ' ===== */\n' + (ROOT / f).read_text(encoding='utf-8') + '\n'
html = html.replace('</body>', '<script>\n' + js + '\n</script>\n</body>')

# --- Images : toutes en data URI + chargement immédiat (aperçu fiable) ---
def attr_repl(m):
    whole, attr, val = m.group(0), m.group(1), m.group(2)
    if val.startswith('data:') or val.startswith(('http:', 'https:', 'mailto:', 'tel:', '#')):
        return whole
    p = ROOT / val.split('?')[0]
    if p.suffix.lower() in ('.jpg', '.jpeg', '.png', '.webp'):
        return f'{attr}="{img_data(p)}"'
    return whole

html = re.sub(r'(src|href|poster|content)="([^"]+\.(?:jpg|jpeg|png|webp))"', attr_repl, html)
html = re.sub(r'\s+loading="lazy"', '', html)
html = html.replace('<html lang="fr"', '<!-- Version autonome : CSS, JS, polices et images intégrés. -->\n<html lang="fr"', 1)

OUT.write_text(html, encoding='utf-8')
print('OK', OUT, round(OUT.stat().st_size / 1024 / 1024, 2), 'Mo')
