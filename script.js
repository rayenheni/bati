/* ==========================================================
   BÂTI-RÉNOV — interactions
   ========================================================== */

/* Adresse de réception des demandes de devis (à remplacer) */
const CONTACT_EMAIL = 'contact@bati-renov.com';

const $  = (sel, ctx = document) => ctx.querySelector(sel);
const $$ = (sel, ctx = document) => Array.from(ctx.querySelectorAll(sel));
const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* ---------- Header au défilement ---------- */
const header = $('#header');
const onScroll = () => header.classList.toggle('is-scrolled', window.scrollY > 40);
onScroll();
window.addEventListener('scroll', onScroll, { passive: true });

/* ---------- Menu mobile ---------- */
const menuToggle = $('#menu-toggle');
const nav = $('#main-nav');

const closeMenu = () => {
  nav.classList.remove('is-open');
  menuToggle.setAttribute('aria-expanded', 'false');
  menuToggle.setAttribute('aria-label', I18N.t('menuOpen'));
};
menuToggle.addEventListener('click', () => {
  const open = nav.classList.toggle('is-open');
  menuToggle.setAttribute('aria-expanded', String(open));
  menuToggle.setAttribute('aria-label', I18N.t(open ? 'menuClose' : 'menuOpen'));
});
$$('a', nav).forEach(link => link.addEventListener('click', closeMenu));
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeMenu(); });
document.addEventListener('click', e => {
  if (!nav.contains(e.target) && !menuToggle.contains(e.target)) closeMenu();
});
window.addEventListener('resize', () => { if (window.innerWidth > 960) closeMenu(); });

/* ---------- Lien de navigation actif ---------- */
const navLinks = $$('.nav-link');
if ('IntersectionObserver' in window) {
  const sectionObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const id = '#' + entry.target.id;
      navLinks.forEach(link => link.classList.toggle('is-active', link.getAttribute('href') === id));
    });
  }, { rootMargin: '-45% 0px -50% 0px' });
  $$('main section[id]').forEach(s => sectionObserver.observe(s));
}

/* ---------- Apparitions au défilement ---------- */
const reveals = $$('.reveal');
const showAllReveals = () => reveals.forEach(el => el.classList.add('is-visible'));

if (reduceMotion || !('IntersectionObserver' in window)) {
  /* Pas d'animation : on ne masque jamais le contenu. */
  showAllReveals();
} else {
  const revealObserver = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });
  reveals.forEach(el => revealObserver.observe(el));

  /* Révèle aussi les éléments déjà franchis (saut d'ancre, restauration de scroll). */
  function revealEntered() {
    $$('.reveal:not(.is-visible)').forEach(el => {
      if (el.getBoundingClientRect().top < window.innerHeight - 20) el.classList.add('is-visible');
    });
  }

  /* N'activer le masquage qu'après avoir vérifié que le mécanisme fonctionne.
     Sans JavaScript (ou si le script échoue), tout reste donc visible. */
  requestAnimationFrame(() => {
    document.documentElement.classList.add('reveal-ready');
    revealEntered();
  });

  window.addEventListener('scroll', revealEntered, { passive: true });
  window.addEventListener('hashchange', revealEntered);
  window.addEventListener('resize', revealEntered);

  /* Filet de sécurité : si aucun élément n'a été révélé, on affiche tout. */
  window.setTimeout(() => {
    if (!document.querySelector('.reveal.is-visible')) {
      showAllReveals();
      document.documentElement.classList.remove('reveal-ready');
    }
  }, 1800);
}

/* ---------- Filtre des réalisations ---------- */
const filters = $$('.filter');
const projectCards = $$('.project-card');
filters.forEach(btn => btn.addEventListener('click', () => {
  const value = btn.dataset.filter;
  filters.forEach(b => {
    const active = b === btn;
    b.classList.toggle('is-active', active);
    b.setAttribute('aria-pressed', String(active));
  });
  projectCards.forEach(card => {
    const show = value === 'all' || card.dataset.category === value;
    card.classList.toggle('is-hidden', !show);
    if (show) card.classList.add('is-visible'); // au cas où la carte n'a pas encore été révélée
  });
}));

/* ---------- Galerie lightbox ---------- */
const lightbox = $('#lightbox');
const lbImg = $('#lightbox-img');
const lbCat = $('#lightbox-cat');
const lbTitle = $('#lightbox-title');
let lightboxItems = [];
let lightboxIndex = 0;
let lastFocused = null;

const visibleCards = () => projectCards.filter(c => !c.classList.contains('is-hidden'));
const cardData = card => ({
  src: $('img', card).getAttribute('src'),
  alt: $('img', card).getAttribute('alt'),
  cat: $('.project-cat', card).textContent,
  title: $('.project-name', card).textContent
});

function renderLightbox() {
  const item = lightboxItems[lightboxIndex];
  lbImg.src = item.src;
  lbImg.alt = item.alt;
  lbCat.textContent = item.cat;
  lbTitle.textContent = item.title;
}
function openLightbox(card) {
  lightboxItems = visibleCards().map(cardData);
  lightboxIndex = Math.max(0, lightboxItems.findIndex(i => i.src === $('img', card).getAttribute('src')));
  lastFocused = card;
  renderLightbox();
  lightbox.hidden = false;
  document.body.classList.add('no-scroll');
  $('#lightbox-close').focus();
}
function closeLightbox() {
  lightbox.hidden = true;
  document.body.classList.remove('no-scroll');
  if (lastFocused) lastFocused.focus();
}
function stepLightbox(delta) {
  if (!lightboxItems.length) return;
  lightboxIndex = (lightboxIndex + delta + lightboxItems.length) % lightboxItems.length;
  renderLightbox();
}
projectCards.forEach(card => card.addEventListener('click', () => openLightbox(card)));
$('#lightbox-close').addEventListener('click', closeLightbox);
$('#lightbox-prev').addEventListener('click', () => stepLightbox(-1));
$('#lightbox-next').addEventListener('click', () => stepLightbox(1));
lightbox.addEventListener('click', e => { if (e.target === lightbox) closeLightbox(); });
document.addEventListener('keydown', e => {
  if (lightbox.hidden) return;
  if (e.key === 'Escape') closeLightbox();
  if (e.key === 'ArrowLeft') stepLightbox(-1);
  if (e.key === 'ArrowRight') stepLightbox(1);
});

/* ---------- Comparateur avant / après ---------- */
const comparison = $('#comparison');
const comparisonRange = $('#comparison-range');
if (comparison && comparisonRange) {
  const updateComparison = () => comparison.style.setProperty('--pos', comparisonRange.value + '%');
  comparisonRange.addEventListener('input', updateComparison);
  updateComparison();
}

/* ---------- Formulaire de contact ---------- */
const form = $('#contact-form');
const formCard = $('#form-card');
const formSuccess = $('#form-success');
const successMail = $('#success-mail');

function setError(field, message) {
  const wrapper = field.closest('.field');
  wrapper.classList.toggle('has-error', Boolean(message));
  $('.error-msg', wrapper).textContent = message || '';
  field.setAttribute('aria-invalid', message ? 'true' : 'false');
}

form.addEventListener('submit', e => {
  e.preventDefault();
  const nom = $('#nom'), email = $('#email'), type = $('#type'), message = $('#message');
  let firstInvalid = null;

  const checks = [
    [nom, nom.value.trim() ? '' : I18N.t('errNom')],
    [email, /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email.value.trim()) ? '' : I18N.t('errEmail')],
    [type, type.value ? '' : I18N.t('errType')],
    [message, message.value.trim().length >= 10 ? '' : I18N.t('errMessage')]
  ];
  checks.forEach(([field, msg]) => {
    setError(field, msg);
    if (msg && !firstInvalid) firstInvalid = field;
  });
  if (firstInvalid) { firstInvalid.focus(); return; }

  const subject = `${I18N.t('subject')}${type.value}`;
  const body = [
    `${I18N.t('labelNom')}${nom.value.trim()}`,
    `${I18N.t('labelTel')}${$('#tel').value.trim() || I18N.t('notProvided')}`,
    `${I18N.t('labelEmail')}${email.value.trim()}`,
    `${I18N.t('labelType')}${type.value}`,
    '',
    I18N.t('labelProject'),
    message.value.trim(),
    '',
    I18N.t('footerMail')
  ].join('\n');
  const href = `mailto:${CONTACT_EMAIL}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;

  successMail.href = href;
  formCard.hidden = true;
  formSuccess.hidden = false;
  successMail.focus();
});

$$('#contact-form input, #contact-form select, #contact-form textarea').forEach(field => {
  field.addEventListener('input', () => setError(field, ''));
});

$('#form-reset').addEventListener('click', () => {
  form.reset();
  $$('.field', form).forEach(f => f.classList.remove('has-error'));
  $$('.error-msg', form).forEach(e => { e.textContent = ''; });
  formSuccess.hidden = true;
  formCard.hidden = false;
  $('#nom').focus();
});

/* ---------- Année courante ---------- */
$('#year').textContent = new Date().getFullYear();

/* ---------- Réactions au changement de langue ---------- */
document.addEventListener('langchange', () => {
  menuToggle.setAttribute('aria-label', I18N.t(nav.classList.contains('is-open') ? 'menuClose' : 'menuOpen'));
  $$('.field.has-error', form).forEach(f => {
    f.classList.remove('has-error');
    const msg = $('.error-msg', f);
    if (msg) msg.textContent = '';
  });
});
