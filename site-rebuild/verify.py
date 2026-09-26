"""Content, SEO and local-resource checks for the static deliverable."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse,unquote
import json,xml.etree.ElementTree as ET
from build import PAGES,ORIGIN
ROOT=Path(__file__).parent/'dist'
class Page(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.h1=0;self.title=False;self.meta={};self.canonical=None;self.ld=[];self.ld_open=False;self.ids=set();self.images=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.add(a['id'])
  if tag=='h1':self.h1+=1
  if tag=='title':self.title=True
  if tag=='meta':self.meta[a.get('name',a.get('property'))]=a.get('content')
  if tag=='link' and a.get('rel')=='canonical':self.canonical=a.get('href')
  if tag=='script' and a.get('type')=='application/ld+json':self.ld_open=True
  if tag=='img':self.images.append(a)
  for attr in ['href','src']:
   if a.get(attr,'').startswith('/'):self.refs.append(a[attr])
  if tag=='img' and a.get('srcset'):
   self.refs.extend(candidate.strip().split()[0] for candidate in a['srcset'].split(','))
  if a.get('data-photo','').startswith('/'):
   self.refs.append(a['data-photo'])
 def handle_data(self,s):
  if self.ld_open:self.ld.append(s)
 def handle_endtag(self,tag):
  if tag=='script':self.ld_open=False
errors=[];titles=set();descs=set()
for route in PAGES:
 file=ROOT/route.strip('/')/'index.html';p=Page();p.feed(file.read_text())
 if p.h1!=1:errors.append(f'{route}: expected one H1, got {p.h1}')
 if p.canonical!=ORIGIN+route:errors.append(f'{route}: wrong canonical')
 if not p.title or not p.meta.get('description'):errors.append(f'{route}: missing metadata')
 if p.meta.get('description') in descs:errors.append(f'{route}: duplicate description')
 descs.add(p.meta.get('description'))
 for block in p.ld:json.loads(block)
 if not p.ld:errors.append(f'{route}: missing schema')
 for im in p.images:
  if not im.get('alt'):errors.append(f'{route}: missing image alt')
 for ref in p.refs:
  parsed=urlparse(ref);path=ROOT/unquote(parsed.path).lstrip('/')
  if path.is_dir():path=path/'index.html'
  if not path.exists():errors.append(f'{route}: missing resource {ref}')
  elif path.suffix=='.webp':
   data=path.read_bytes()
   if len(data)<20 or data[:4]!=b'RIFF' or data[8:12]!=b'WEBP':errors.append(f'{route}: invalid WebP {ref}')
  elif parsed.fragment and path.suffix=='.html':
   target=Page();target.feed(path.read_text())
   if parsed.fragment not in target.ids:errors.append(f'{route}: missing anchor {ref}')
ET.parse(ROOT/'sitemap.xml')
ET.parse(ROOT/'image-sitemap.xml')
for path in (ROOT/'assets').glob('*.webp'):
 data=path.read_bytes()
 if len(data)<20 or data[:4]!=b'RIFF' or data[8:12]!=b'WEBP':errors.append(f'invalid WebP asset: {path.name}')
for file in (ROOT/'assets').glob('*.svg'):ET.parse(file)
assert not errors,'\n'.join(errors)
print(f'PASS: {len(PAGES)} pages; one H1 each; unique descriptions; canonical and JSON-LD metadata; local links, anchors, images, styles, scripts; XML and SVG syntax.')
