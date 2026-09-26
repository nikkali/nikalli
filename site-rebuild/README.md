# Relevant Design website

Production static site for relevantdesign.cc, copied from the Relevant Design — One Zillion Possibilities Site. The published files are in `dist/`; `build.py` regenerates their HTML and SEO metadata with `SITE_URL=https://relevantdesign.cc`.

To update: edit `build.py`, run `SITE_URL=https://relevantdesign.cc python3 build.py` and `SITE_URL=https://relevantdesign.cc python3 verify.py`, then commit the source and generated `dist/` together. The inquiry form opens an email message and requires the visitor to send it.
