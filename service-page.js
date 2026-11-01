/* Interactions partagées par les pages de service (menu + en-tête). */
(() => {
  'use strict';
  const header = document.querySelector('#header');
  const toggle = document.querySelector('#menu-toggle');
  const nav = document.querySelector('#main-nav');

  const updateHeader = () => {
    if (header) header.classList.toggle('is-scrolled', window.scrollY > 40);
  };
  updateHeader();
  window.addEventListener('scroll', updateHeader, { passive: true });

  if (!toggle || !nav) return;
  const syncLabel = () => {
    const open = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-label', window.I18N ? window.I18N.t(open ? 'menuClose' : 'menuOpen') : (open ? 'Fermer le menu' : 'Ouvrir le menu'));
  };
  const closeMenu = () => {
    nav.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
    syncLabel();
  };

  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded', String(open));
    syncLabel();
  });
  nav.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  document.addEventListener('keydown', event => { if (event.key === 'Escape') closeMenu(); });
  document.addEventListener('click', event => {
    if (!nav.contains(event.target) && !toggle.contains(event.target)) closeMenu();
  });
  window.addEventListener('resize', () => { if (window.innerWidth > 960) closeMenu(); });
  document.addEventListener('langchange', syncLabel);
})();
