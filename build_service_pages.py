#!/usr/bin/env python3
"""Build the six static bilingual BÂTI-RÉNOV service pages."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent

PAGES = [
    {
        "slug": "renovation-appartements",
        "code": "01",
        "title": "Rénovation d'appartements",
        "title_ar": "ترميم الشقق",
        "image": "about.jpg",
        "alt": "Chantier de rénovation intérieure",
        "hero": "Une rénovation soignée, de la préparation du chantier aux finitions.",
        "hero_ar": "ترميم متقن، من إعداد الورشة إلى التشطيبات النهائية.",
        "lead": "Nous rénovons les appartements de façon complète ou ciblée, selon l'état du lieu, vos besoins et le résultat recherché.",
        "lead_ar": "نجدّد الشقق بشكل كامل أو جزئي، وفق حالة المكان واحتياجاتكم والنتيجة التي ترغبون فيها.",
        "body": "Nous coordonnons les étapes du chantier et les différents corps de métier pour assurer une réalisation cohérente, avec une attention constante portée à la qualité et aux finitions.",
        "body_ar": "ننسّق مراحل الورشة ومختلف الحرف لضمان تنفيذ متناسق، مع عناية مستمرة بالجودة والتشطيبات.",
        "meta": "Rénovation d'appartements : travaux complets ou ciblés, coordination des corps de métier et finitions soignées avec BÂTI-RÉNOV.",
        "meta_ar": "ترميم الشقق في تونس الكبرى: ترميم كامل أو جزئي، وتنسيق الأشغال وتشطيبات متقنة مع باتي-رينوف.",
        "points": [
            ("Préparation & diagnostic", "Évaluer le logement, définir les priorités et organiser les travaux avant le démarrage."),
            ("Rénovation ciblée ou complète", "Une intervention adaptée à l'état de l'appartement, à vos besoins et à votre budget."),
            ("Coordination des finitions", "Un suivi attentif des différents corps de métier jusqu'aux dernières finitions."),
        ],
    },
    {
        "slug": "construction-villas",
        "code": "02",
        "title": "Construction de villas",
        "title_ar": "بناء الفيلات",
        "image": "project-villa.jpg",
        "alt": "Villa contemporaine avec piscine au crépuscule",
        "hero": "Construire une villa pensée pour votre quotidien, de l'étude à la livraison.",
        "hero_ar": "نبني فيلا تناسب حياتكم اليومية، من الدراسة إلى التسليم.",
        "lead": "Nous coordonnons les différentes étapes de la construction de votre villa, des premiers travaux aux finitions.",
        "lead_ar": "ننسّق مختلف مراحل بناء فيلتكم، من الأشغال الأولى إلى التشطيبات.",
        "body": "Chaque étape est suivie avec un interlocuteur dédié, pour garder une vision cohérente du chantier, des matériaux et des finitions.",
        "body_ar": "تُتابع كل مرحلة من خلال مخاطب واحد للحفاظ على رؤية متناسقة للورشة والمواد والتشطيبات.",
        "meta": "Construction de villas : préparation du projet, coordination des étapes de chantier et finitions suivies avec BÂTI-RÉNOV.",
        "meta_ar": "بناء الفيلات في تونس الكبرى: متابعة مراحل المشروع وتنسيق أشغال البناء والتشطيبات مع باتي-رينوف.",
        "points": [
            ("Étude & planification", "Définir les besoins, les choix techniques et le déroulement du projet de construction."),
            ("Gros œuvre & coordination", "Coordonner les étapes du chantier pour bâtir une villa cohérente, du gros œuvre aux interventions intérieures."),
            ("Second œuvre & finitions", "Suivre les espaces intérieurs, les détails de finition et la préparation à la livraison."),
        ],
    },
    {
        "slug": "reamenagement-logements",
        "code": "03",
        "title": "Réaménagement de logements",
        "title_ar": "إعادة تهيئة المساكن",
        "image": "project-living.jpg",
        "alt": "Séjour réaménagé aux tons crème et chêne clair",
        "hero": "Réorganiser votre logement pour mieux vivre chaque espace.",
        "hero_ar": "نعيد تنظيم مسكنكم للاستفادة الأفضل من كل مساحة.",
        "lead": "Nous repensons les volumes, la circulation et les usages pour faire évoluer votre logement selon vos besoins.",
        "lead_ar": "نعيد التفكير في المساحات وحركة التنقل والاستخدامات لتطوير مسكنكم وفق احتياجاتكم.",
        "body": "De l'étude des possibilités aux finitions, nous coordonnons les interventions nécessaires pour une transformation harmonieuse.",
        "body_ar": "من دراسة الإمكانيات إلى التشطيبات، ننسّق التدخلات اللازمة لتحويل متناسق.",
        "meta": "Réaménagement de logements : optimiser les volumes, la circulation et le confort selon vos besoins avec BÂTI-RÉNOV.",
        "meta_ar": "إعادة تهيئة المساكن: تحسين المساحات وحركة التنقل والضوء والراحة وفق احتياجاتكم، مع باتي-رينوف.",
        "points": [
            ("Organisation des volumes", "Repenser la circulation et l'usage de chaque pièce pour un quotidien plus fluide."),
            ("Lumière & confort", "Faire évoluer l'ambiance et le confort du logement en fonction de vos priorités."),
            ("Travaux & finitions", "Coordonner les transformations et soigner la cohérence des finitions."),
        ],
    },
    {
        "slug": "espaces-professionnels",
        "code": "04",
        "title": "Surfaces professionnelles",
        "title_ar": "المساحات المهنية",
        "image": "project-office.jpg",
        "alt": "Espace professionnel réaménagé en bureaux ouverts",
        "hero": "Des espaces professionnels conçus autour de votre activité.",
        "hero_ar": "مساحات مهنية مصممة بما يتناسب مع نشاطكم.",
        "lead": "Nous réaménageons bureaux, commerces et espaces collectifs selon les usages et les contraintes du lieu.",
        "lead_ar": "نعيد تهيئة المكاتب والمحلات والفضاءات الجماعية وفق الاستخدامات وخصوصية المكان.",
        "body": "Le projet est organisé avec vous pour optimiser les espaces, la circulation et le confort, tout en portant une attention particulière aux finitions.",
        "body_ar": "ننظم المشروع معكم لتحسين المساحات وحركة التنقل والراحة، مع عناية خاصة بالتشطيبات.",
        "meta": "Aménagement de bureaux, commerces et surfaces professionnelles : organisation des espaces, coordination des travaux et finitions avec BÂTI-RÉNOV.",
        "meta_ar": "تهيئة المكاتب والمحلات والفضاءات المهنية بما يتلاءم مع نشاطكم ومتطلبات المكان، مع باتي-رينوف.",
        "points": [
            ("Aménagement des espaces", "Organiser les bureaux, commerces ou espaces collectifs selon votre activité."),
            ("Interventions planifiées", "Coordonner les étapes du chantier en tenant compte du fonctionnement du lieu."),
            ("Confort & finitions", "Soigner la circulation, les usages et l'accueil de vos équipes et visiteurs."),
        ],
    },
    {
        "slug": "ascenseurs",
        "code": "05",
        "title": "Ascenseurs",
        "title_ar": "المصاعد",
        "image": "service-elevator.jpg",
        "alt": "Illustration d'un technicien réalisant la maintenance d'un ascenseur",
        "hero": "Installation et maintenance des ascenseurs.",
        "hero_ar": "صيانة و تركيز المصاعد.",
        "lead": "Nous proposons l'installation et la maintenance des ascenseurs pour vos projets de bâtiment.",
        "lead_ar": "نقدم خدمات تركيب وصيانة المصاعد لمشاريع المباني.",
        "body": "Contactez-nous pour préciser votre besoin et le type d'installation ou de maintenance recherché.",
        "body_ar": "تواصلوا معنا لتحديد احتياجاتكم ونوع التركيب أو الصيانة المطلوبة.",
        "meta": "Installation et maintenance des ascenseurs pour vos projets de bâtiment avec BÂTI-RÉNOV. Contactez-nous pour préciser votre besoin.",
        "meta_ar": "صيانة و تركيز المصاعد للمباني والمشاريع في تونس الكبرى، مع باتي-رينوف.",
        "points": [
            ("Étude de l'installation", "Préciser le besoin et les caractéristiques du bâtiment avant de définir l'intervention."),
            ("Installation", "Une installation étudiée selon le projet et la configuration du bâtiment."),
            ("Maintenance des ascenseurs", "Une intervention d'entretien pour accompagner le fonctionnement de votre équipement."),
        ],
    },
    {
        "slug": "jardins-espaces-verts",
        "code": "06",
        "title": "Jardins & espaces verts",
        "title_ar": "الحدائق والمساحات الخضراء",
        "image": "jardin-amenagement.jpg",
        "alt": "Jardin méditerranéen aménagé avec allée en pierre, oliviers et lavande",
        "hero": "Entretien et décoration des jardins et espaces verts.",
        "hero_ar": "صيانة وتزيين الحدائق والمساحات الخضراء.",
        "lead": "Nous créons, plantons et entretenons vos jardins, des massifs et allées à l'arrosage, la taille et la décoration.",
        "lead_ar": "نصمم حدائقكم ونزرعها ونعتني بها، من الأحواض والممرات إلى الري والتقليم والديكور.",
        "body": "Le service s'adapte à la taille de l'espace et au niveau d'entretien souhaité, en veillant à l'harmonie des plantations et des finitions paysagères.",
        "body_ar": "تتكيف الخدمة مع مساحة الحديقة ومستوى العناية المطلوب، مع الحرص على تناسق النباتات والتشطيبات الطبيعية.",
        "meta": "Création, entretien et décoration de jardins et espaces verts : plantations, taille, arrosage et aménagement paysager avec BÂTI-RÉNOV.",
        "meta_ar": "صيانة وتزيين الحدائق والمساحات الخضراء: التصميم والزراعة والعناية الموسمية مع باتي-رينوف.",
        "points": [
            ("Création & aménagement", "Conception de jardins, allées, pelouses, massifs et terrasses plantées."),
            ("Plantation & arrosage", "Choix des essences, plantation, paillage et gestion de l'arrosage."),
            ("Tonte & taille", "Entretien régulier des pelouses, haies, arbustes et élagage raisonné."),
        ],
    },
]

NAV = [
    ("Accueil", "../index.html#accueil"),
    ("Expertise", "../index.html#expertise"),
    ("Services", "../index.html#services"),
    ("Jardins", "../index.html#jardins"),
    ("Réalisations", "../index.html#realisations"),
    ("Méthode", "../index.html#methode"),
    ("Contact", "../index.html#contact"),
]
SERVICE_LINKS = [
    ("Rénovation d'appartements", "renovation-appartements.html"),
    ("Construction de villas", "construction-villas.html"),
    ("Réaménagement de logements", "reamenagement-logements.html"),
    ("Surfaces professionnelles", "espaces-professionnels.html"),
    ("Ascenseurs", "ascenseurs.html"),
    ("Jardins & espaces verts", "jardins-espaces-verts.html"),
]


def h(value):
    return escape(value, quote=True)


def render_page(page):
    title = page["title"]
    title_ar = page["title_ar"]
    image_width, image_height = {
        "service-elevator.jpg": (1086, 1448),
        "jardin-amenagement.jpg": (1672, 941),
    }.get(page["image"], (1448, 1086))
    doc_title = f"BÂTI-RÉNOV — {title}"
    doc_title_ar = f"باتي-رينوف — {title_ar}"
    nav_links = "\n".join(
        f'      <a href="{href}" class="nav-link{" is-active" if label == "Services" else ""}"{" aria-current=\"page\"" if label == "Services" else ""}>{h(label)}</a>'
        for label, href in NAV
    )
    service_links = "\n".join(
        f'        <a href="{href}">{h(label)}</a>' for label, href in SERVICE_LINKS
    )
    point_cards = "\n".join(
        f'''        <article class="service-detail-card">
          <span class="service-detail-card-number" aria-hidden="true">{i:02d}</span>
          <h3>{h(label)}</h3>
          <p>{h(description)}</p>
        </article>'''
        for i, (label, description) in enumerate(page["points"], 1)
    )
    return f'''<!DOCTYPE html>
<html lang="fr" dir="ltr">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title data-fr="{h(doc_title)}" data-ar="{h(doc_title_ar)}">{h(doc_title)}</title>
<meta name="description" content="{h(page['meta'])}" data-fr="{h(page['meta'])}" data-ar="{h(page['meta_ar'])}" />
<meta name="theme-color" content="#008397" />
<meta property="og:title" content="{h(doc_title)}" data-fr="{h(doc_title)}" data-ar="{h(doc_title_ar)}" />
<meta property="og:description" content="{h(page['meta'])}" data-fr="{h(page['meta'])}" data-ar="{h(page['meta_ar'])}" />
<meta property="og:image" content="../assets/{h(page['image'])}" />
<meta property="og:locale" content="fr_TN" />
<meta property="og:locale:alternate" content="ar_TN" />
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='10' fill='%230e2b32'/%3E%3Cpath d='M18 46V18h16a9 9 0 0 1 0 18H18m0 0h20a9 9 0 0 1 0 18H18' fill='none' stroke='%237cd3e0' stroke-width='5' stroke-linejoin='round'/%3E%3Ccircle cx='48' cy='15' r='6' fill='%23e3a0be'/%3E%3C/svg%3E" />
<link rel="preload" href="../assets/{h(page['image'])}" as="image" />
<link rel="stylesheet" href="../fonts/fonts.css" />
<link rel="stylesheet" href="../styles.css?v=20261030-6" />
<link rel="stylesheet" href="../rtl.css?v=20261030-6" />
</head>
<body>
<a class="skip-link" href="#contenu">Aller au contenu</a>

<header class="site-header" id="header">
  <div class="container header-inner">
    <a class="brand" href="../index.html#accueil" aria-label="BÂTI-RÉNOV, retour à l'accueil">
      <span class="brand-mark" aria-hidden="true">
        <svg viewBox="0 0 48 48" fill="none"><rect x="1" y="1" width="46" height="46" rx="6" stroke="currentColor" stroke-width="1.6"/><path d="M15 34V14h10.5a6.6 6.6 0 0 1 0 13.2H15m0 0h13a6.8 6.8 0 0 1 0 13.6H15" stroke="currentColor" stroke-width="2.6" stroke-linecap="square" stroke-linejoin="miter"/></svg>
      </span>
      <span class="brand-text"><strong>BÂTI-RÉNOV</strong><small>BÂTIMENT &amp; FINITIONS</small></span>
    </a>

    <nav class="main-nav" id="main-nav" aria-label="Navigation principale">
{nav_links}
      <a href="../index.html#contact" class="btn btn-primary nav-cta">Demander un devis <span aria-hidden="true">↗</span></a>
    </nav>

    <div class="header-tools">
      <div class="lang-switch" role="group" aria-label="Choisir la langue">
        <button type="button" class="lang-btn is-active" data-lang="fr" aria-pressed="true" aria-label="Français" lang="fr">FR</button>
        <span class="lang-divider" aria-hidden="true"></span>
        <button type="button" class="lang-btn" data-lang="ar" aria-pressed="false" aria-label="العربية" lang="ar" dir="rtl">ع</button>
      </div>
      <button class="menu-toggle" id="menu-toggle" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="main-nav">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>

<main id="contenu">
  <section class="service-detail-hero" aria-labelledby="service-title">
    <img class="service-detail-image" src="../assets/{h(page['image'])}" alt="{h(page['alt'])}" width="{image_width}" height="{image_height}" fetchpriority="high" />
    <div class="service-detail-scrim" aria-hidden="true"></div>
    <div class="container service-detail-inner">
      <nav class="service-breadcrumb" aria-label="Fil d'Ariane">
        <a href="../index.html#accueil">Accueil</a><span aria-hidden="true">›</span>
        <a href="../index.html#services">Services</a><span aria-hidden="true">›</span>
        <span aria-current="page">{h(title)}</span>
      </nav>
      <div class="service-detail-heading">
        <p class="eyebrow eyebrow-light"><span class="eyebrow-line" aria-hidden="true"></span><span class="eyebrow-text">Nos savoir-faire</span></p>
        <p class="service-detail-index">{page['code']} <span aria-hidden="true">/</span> 06</p>
        <h1 class="service-detail-title" id="service-title">{h(title)}</h1>
        <p class="service-detail-lead">{h(page['hero'])}</p>
        <div class="service-detail-actions">
          <a href="../index.html#contact" class="btn btn-primary btn-lg">Demander un devis <span aria-hidden="true">↗</span></a>
          <a href="../index.html#services" class="btn btn-ghost btn-lg">Tous nos services <span aria-hidden="true">→</span></a>
        </div>
      </div>
    </div>
  </section>

  <section class="section service-detail-overview" aria-labelledby="overview-title">
    <div class="container service-detail-overview-grid">
      <div class="service-detail-overview-main">
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span> Notre approche</p>
        <h2 class="h2" id="overview-title">Une prestation adaptée à votre projet.</h2>
        <p class="lead">{h(page['lead'])}</p>
        <p>{h(page['body'])}</p>
      </div>
      <aside class="service-detail-aside" aria-labelledby="service-aside-label">
        <span class="service-detail-aside-mark" aria-hidden="true">✳</span>
        <p class="eyebrow" id="service-aside-label">Votre projet, notre engagement</p>
        <h3>Suivi rigoureux</h3>
        <p>Un pilotage de chantier constant, jusqu'à la réception.</p>
      </aside>
    </div>
  </section>

  <section class="section service-detail-scope" aria-labelledby="scope-title">
    <div class="container">
      <div class="service-detail-scope-head">
        <div>
          <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span> Dans le détail</p>
          <h2 class="h2" id="scope-title">Notre prestation</h2>
        </div>
        <p class="service-detail-scope-note">Décrivez-nous votre besoin. Nous vous répondons avec une première étude et un devis personnalisé.</p>
      </div>
      <div class="service-detail-scope-grid">
{point_cards}
      </div>
    </div>
  </section>

  <section class="cta-band service-detail-cta">
    <div class="container cta-band-inner">
      <div>
        <p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span> Votre projet commence ici</p>
        <h2>Parlons de<br /><em>votre projet.</em></h2>
      </div>
      <div class="cta-band-side">
        <p>Décrivez-nous votre besoin. Nous vous répondons avec une première étude et un devis personnalisé.</p>
        <a href="../index.html#contact" class="btn btn-light">Demander un devis gratuit <span aria-hidden="true">↗</span></a>
      </div>
    </div>
  </section>
</main>

<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-brand">
        <a class="brand brand-footer" href="../index.html#accueil" aria-label="BÂTI-RÉNOV, retour à l'accueil">
          <span class="brand-mark" aria-hidden="true">
            <svg viewBox="0 0 48 48" fill="none"><rect x="1" y="1" width="46" height="46" rx="6" stroke="currentColor" stroke-width="1.6"/><path d="M15 34V14h10.5a6.6 6.6 0 0 1 0 13.2H15m0 0h13a6.8 6.8 0 0 1 0 13.6H15" stroke="currentColor" stroke-width="2.6" stroke-linejoin="miter"/></svg>
          </span>
          <span class="brand-text"><strong>BÂTI-RÉNOV</strong><small>BÂTIMENT &amp; FINITIONS</small></span>
        </a>
        <p>Construction générale • Rénovation • Réaménagement • Ascenseurs.<br />Des solutions clés en main, de A à Z.</p>
        <p class="footer-claim">Votre projet, notre engagement,<br /><em>l'excellence en réalisation.</em></p>
      </div>
      <div class="footer-col">
        <h4>Navigation</h4>
        <a href="../index.html#accueil">Accueil</a><a href="../index.html#expertise">Expertise</a><a href="../index.html#services">Services</a><a href="../index.html#jardins">Jardins</a><a href="../index.html#realisations">Réalisations</a><a href="../index.html#methode">Méthode</a><a href="../index.html#contact">Contact</a>
      </div>
      <div class="footer-col">
        <h4>Savoir-faire</h4>
{service_links}
      </div>
      <div class="footer-col footer-contact">
        <h4>Nous joindre</h4>
        <a href="tel:+21624231201">+216 24 231 201</a>
        <a href="mailto:contact@bati-renov.com">contact@bati-renov.com</a>
        <p>Grand Tunis &amp; environs</p>
        <a href="../index.html#contact" class="btn btn-outline btn-outline-light">Nous écrire <span aria-hidden="true">↗</span></a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span id="year">2026</span> BÂTI-RÉNOV. Tous droits réservés.</span>
      <span>Qualité · Fiabilité · Esthétisme · Finitions</span>
      <a href="#contenu" class="back-top">Retour en haut ↑</a>
    </div>
  </div>
</footer>

<script src="../i18n.js"></script>
<script src="../service-page.js"></script>
</body>
</html>
'''


def main():
    target = ROOT / "services"
    target.mkdir(exist_ok=True)
    for page in PAGES:
        path = target / f"{page['slug']}.html"
        path.write_text(render_page(page), encoding="utf-8")
        print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
