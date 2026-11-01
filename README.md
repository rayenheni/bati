# BÂTI-RÉNOV — site vitrine

Site vitrine moderne, responsive et **bilingue français / arabe**, entièrement statique
(HTML / CSS / JavaScript, sans dépendance externe).
Tous les visuels et toutes les polices sont inclus localement : le site fonctionne hors ligne.

## Aperçu

Ouvrez `index.html` dans un navigateur, ou lancez un serveur local :

```bash
cd bati-renov
python3 -m http.server 8000
# puis http://localhost:8000
```

> **Aperçu / déploiement** : le site est 100 % statique, donc aucun build n'est nécessaire. Les
> animations d'apparition au scroll sont une amélioration progressive : si JavaScript est bloqué
> (iframe sandbox, module désactivé, script non chargé), tout le contenu reste visible et lisible.
> Les interactions (menu, filtres, lightbox, formulaire, sélecteur de langue) nécessitent
> JavaScript — utilisez un vrai serveur HTTP pour les tester.

### Aperçu autonome (zéro dépendance)

`apercu-autonome.html` est une **copie compilée de la page d'accueil en un seul fichier** : CSS,
JavaScript, polices et images y sont intégrés en data URI. Il s'ouvre directement (double-clic,
`file://`), fonctionne hors ligne et dans une iframe sandbox sans accès réseau — utile pour les aperçus
qui n'arrivent pas à charger les fichiers relatifs. Les six pages détaillées restent des fichiers
séparés dans `services/` ; servez le dossier du site pour les parcourir. C'est un fichier généré :
après modification des sources, relancer

```bash
python3 build_standalone.py   # nécessite Pillow
```

Pour la mise en production, déployez les fichiers sources (`index.html`, `services/`, `styles.css`,
`rtl.css`, `i18n.js`, `script.js`, `service-page.js`, `fonts/`, `assets/`) : les six URL de service
et les liens relatifs resteront ainsi fonctionnels, avec les images en qualité maximale.

## Structure

```
bati-renov/
├── index.html             # Accueil et sections principales (texte source en français)
├── services/               # Six pages détaillées, bilingues, une par service
├── build_service_pages.py  # Générateur des pages statiques de service
├── service-page.js         # Interactions du menu et de l'en-tête sur ces pages
├── styles.css              # Design system, mise en page et responsive (cache-busté)
├── rtl.css                 # Surcharges RTL (chargées après styles.css)
├── i18n.js                 # Dictionnaire FR → AR + moteur de bascule de langue et SEO
├── script.js               # Menu, filtres, lightbox, comparateur, formulaire d'accueil
├── fonts/                  # Manrope, Cormorant Garamond, Tajawal (woff2 locaux)
├── assets/                 # Visuels de la maquette
└── README.md
```

Les pages HTML de `services/` sont statiques. Après modification des contenus dans `build_service_pages.py`,
les régénérer avec `python3 build_service_pages.py`.

Sections : Accueil (hero) • Bandeau d'engagements • Expertise • Services (six cartes ordinaires)
• **Détails Jardins & espaces verts** • Réalisations filtrables • Comparateur avant/après • Méthode en 4 étapes
• Bandeau d'appel à l'action • Contact + formulaire • Pied de page. Chaque carte de service mène désormais
à sa propre page bilingue dans `services/` : rénovation d'appartements, construction de villas,
réaménagement de logements, surfaces professionnelles, ascenseurs et jardins / espaces verts.
Les CTA des pages de service renvoient au formulaire de contact de la page d'accueil.

L'activité jardins apparaît comme une carte ordinaire — au même format que les autres — dans la
grille Services. La carte mène à `services/jardins-espaces-verts.html`, tandis que la section détaillée
reste sur l'accueil avec 4 prestations (création & aménagement, tonte & taille, plantation & arrosage,
décoration & lumière) et une galerie de 3 visuels. Les visuels correspondants sont
`assets/jardin-*.jpg` ; la police arabe **Tajawal** est embarquée dans `fonts/` pour un
affichage correct hors ligne.

L'activité **ascenseurs** est intégrée au catalogue des services, avec sa propre page
`services/ascenseurs.html`, une carte photo, une traduction FR/AR, un choix dédié dans le formulaire
et un lien depuis le pied de page. La prestation affichée est « Installation et maintenance des
ascenseurs » / « صيانة و تركيز المصاعد ». Le visuel `assets/service-elevator.jpg` est une illustration
de maquette, pas une photo de chantier réel.

Fonctionnalités : six pages de service détaillées avec métadonnées localisées, navigation fixe qui change
au scroll, menu mobile, animations d'apparition au scroll, filtres de galerie, lightbox navigable au clavier,
curseur avant/après (souris + tactile + clavier), formulaire avec validation et respect de
`prefers-reduced-motion`. Les pages de service restent lisibles sans JavaScript ; le sélecteur de langue
et le menu mobile nécessitent JavaScript.

## Bilingue français / arabe

Le sélecteur **FR | ع** en haut à droite (à gauche en arabe) bascule instantanément toute l'interface,
sans rechargement de page. En mode arabe :

- `<html lang="ar" dir="rtl">` est activé et `rtl.css` inverse les alignements, bordures, dégradés,
  badges, flèches et boutons de la lightbox ;
- les titres, textes, libellés du formulaire, options, messages d'erreur, `alt`, `placeholder`,
  `aria-label`, `<title>` et balises Open Graph sont traduits ;
- la police **Tajawal** remplace les polices latines, avec un interlignage adapté et
  l'espacement des lettres neutralisé (l'arabe est une écriture liée) ;
- le comparateur avant/après reste en LTR pour garder un curseur intuitif, mais ses libellés sont arabes.

Le choix est mémorisé dans `localStorage` et reflété dans l'URL : `index.html?lang=ar` ouvre
directement la version arabe (pratique à partager). Les numéros de téléphone et adresses e-mail sont
forcés en LTR pour éviter les inversions bidi.

**Modifier une traduction** : toutes les traductions sont dans `i18n.js` — les objets `FR_TO_AR`
(textes), `ATTR` (attributs), `META` (balises SEO) et `DYN` (chaînes générées par JavaScript).
Les clés sont les textes français d'origine : si vous modifiez un texte dans `index.html`, mettez la
clé correspondante à jour dans `i18n.js`. Les chaînes dynamiques (erreurs du formulaire, objet du
mail) sont lues via `I18N.t('clé')` dans `script.js`.

> Pour un référencement optimal en production, prévoyez deux URL distinctes (par ex. `/fr/` et
> `/ar/`) avec des balises `hreflang`, plutôt que le paramètre `?lang=`.

**Changer la police arabe** : les huit fichiers `fonts/tajawal-*.woff2` (graisses 400/500/700/800,
sous-ensembles `arabic` et `latin`) sont déclarés dans `fonts/fonts.css`. Pour une autre police,
remplacez ces fichiers, adaptez les règles `@font-face`, puis modifiez la variable
`--arab` dans `:root` (`styles.css`). Les ajustements de taille et d'interlignage propres à l'arabe
se trouvent dans `rtl.css`.

## À remplacer avant la mise en ligne

Le téléphone affiché a été fourni et confirmé ; les autres coordonnées de la liste restent des **placeholders à vérifier** avant la mise en ligne :

| Élément | Où le modifier |
| --- | --- |
| Téléphone `+216 24 231 201` (confirmé) | `index.html` + pied de page des pages `services/` |
| E-mail `contact@bati-renov.com` | `index.html`, pages `services/` **et** `script.js` → `CONTACT_EMAIL` |
| Zone d'intervention `Grand Tunis & environs` | `index.html` (contact + pied de page) et pages `services/` |
| Horaires | `index.html` (section contact) |
| Nom de domaine `bati-renov.com` dans le corps du mail | `script.js` |
| Visuels de démonstration | remplacer les fichiers dans `assets/` (garder les mêmes noms) |
| Textes traduits | `i18n.js` (si vous modifiez le français dans `index.html` ou `services/`) |
| Mentions légales / politique de confidentialité | à ajouter selon votre situation juridique |

### Le formulaire de contact

Il s'agit d'un site statique : le formulaire ne peut pas envoyer d'e-mail tout seul. À la soumission,
il valide les champs puis génère un lien `mailto:` pré-rempli — le visiteur confirme l'envoi depuis sa
messagerie. Pour un envoi direct, connectez le formulaire à un service (Formspree, Netlify Forms,
Web3Forms, ou votre propre backend) en remplaçant le bloc `form.addEventListener('submit', …)` dans
`script.js`.

### Avant / Après

Le comparateur utilise la même photo avec un filtre pour simuler l'« avant ». Remplacez l'image de
`.comparison-before` par une vraie photo de chantier (et retirez la règle `filter:` correspondante
dans `styles.css`) pour un rendu authentique.

## Personnalisation rapide

Les couleurs et la typographie sont définies en haut de `styles.css` dans `:root` :

```css
--teal:#008397;      /* couleur dominante — bleu turquoise */
--magenta:#821a4d;   /* accent secondaire — pourpre ennabi */
--ink:#0e2b32;       /* texte et fonds sombres (bleu-vert profond) */
--paper:#f5f9f9;     /* fond clair froid */
```

Le turquoise pilote les boutons, filets, icônes et états actifs ; l'ennabi colore les mots en
italique, les citations et quelques accents décoratifs. Deux variantes éclaircies
(`--teal-on-dark`, `--magenta-on-dark`) assurent la lisibilité sur les fonds sombres.
