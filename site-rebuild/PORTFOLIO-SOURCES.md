# Portfolio refresh — September 26, 2026

The public site uses original portfolio photography and existing customer design presentations. No new AI images were generated for this refresh. Captions distinguish installed-work photographs, design artwork, and mockups; a mockup does not imply a completed installation or a photographed customer.

## Previously published Relevant Design archive

Images come from this repository's `assets/imgs/` archive: Jones truck graphics, Helanbak pickup graphics, Keep Moving container lettering, Woodlawn pole banners and welcome sign, Marion County school branding, Richland Creek apparel presentation, Premiere Companies logo, Farmers Med Shoppe flag presentation, Stateline Church branding, and event display installation. Existing Woodlawn interior display, downtown Columbia event, and Orchard Park website assets remain in use.

## Existing design archive in Google Drive

Selected files: `t-shirt-mockup-featuring-a-bearded-man-leaning-against-a-rusty-wall-32841 (1).png` (Quick Cash Pawn), `unisex-t-shirt-mockup-featuring-a-happy-girl-with-a-trendy-outfit-22962 (2).png` (Bug Me), `Royalty Painting Business Cards 2017 mockup new.png`, and `COLUMBIA ACADEMY DRUMLINE SHIRTS 2026.png`.

Other retrieved files were reviewed but not used. Public Facebook retrieval was blocked; no Facebook images were scraped or attributed without inspection. Private customer records, work orders, and financial material were excluded.

## Implementation

15 additional optimized WebP images; responsive 640px versions where useful; intrinsic image dimensions; lazy loading below the fold; an 18-item filterable portfolio with an accessible full-image viewer; service-specific galleries; descriptive captions and alt text; image sitemap; service and image structured data; canonical production URLs; existing redirects retained.

Keep generated `dist/` and source changes together. Build with `SITE_URL=https://relevantdesign.cc python3 build.py`, then run `python3 verify.py` and `node --check dist/site.js`. Netlify publishes the committed `site-rebuild/dist` output.
