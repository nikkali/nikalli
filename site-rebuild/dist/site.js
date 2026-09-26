const menu=document.querySelector('.menu-button');const nav=document.querySelector('.nav');
function closeMenu(){nav?.classList.remove('open');menu?.setAttribute('aria-expanded','false');if(menu)menu.textContent='Menu +'}
menu?.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open);menu.textContent=open?'Close −':'Menu +'});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&menu?.getAttribute('aria-expanded')==='true'){closeMenu();menu.focus()}});
nav?.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));
document.querySelectorAll('[data-filter]').forEach(button=>button.addEventListener('click',()=>{document.querySelectorAll('[data-filter]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));let count=0;document.querySelectorAll('[data-category]').forEach(card=>{const show=button.dataset.filter==='all'||card.dataset.category===button.dataset.filter;card.hidden=!show;if(show)count++});const status=document.getElementById('work-status');if(status)status.textContent=`Showing ${count} projects.`}));
const form=document.getElementById('quote-form');
if(form){const params=new URLSearchParams(location.search);const service=params.get('service');const select=form.elements.service;if(service&&[...select.options].some(x=>x.value===service))select.value=service;
form.addEventListener('submit',event=>{event.preventDefault();if(!form.reportValidity())return;const d=new FormData(form);const subject=`Project inquiry — ${d.get('service')}`;const body=`Hello Relevant Design,\n\nI'd like to talk about a project.\n\nName: ${d.get('name')}\nBusiness / organization: ${d.get('company')||'Not specified'}\nEmail: ${d.get('email')}\nPhone: ${d.get('phone')||'Not specified'}\nService: ${d.get('service')}\nNeeded by: ${d.get('deadline')||'Flexible'}\n\nProject details:\n${d.get('details')}\n\nThank you!`;const link=`mailto:discover@relevantdesign.cc?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;window.location.href=link;const status=document.getElementById('quote-status');status.replaceChildren(document.createTextNode('Your email draft is ready. Send it from your email app to complete your inquiry. If the app did not open, '));const a=document.createElement('a');a.href=link;a.textContent='open the draft again';status.append(a,document.createTextNode(' or call (601) 736-0663. Nothing has been sent by this website.'));});}

const viewer=document.getElementById('portfolio-viewer');
if(viewer){
 let opener;
 document.querySelectorAll('[data-photo]').forEach(button=>button.addEventListener('click',()=>{
  opener=button;
  const image=viewer.querySelector('img');
  image.src=button.dataset.photo;
  image.alt=button.querySelector('img').alt;
  viewer.querySelector('.viewer-caption').textContent=button.dataset.caption;
  viewer.showModal();
 }));
 viewer.querySelector('.viewer-close').addEventListener('click',()=>viewer.close());
 viewer.addEventListener('click',event=>{if(event.target===viewer){const r=viewer.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)viewer.close()}});
 viewer.addEventListener('close',()=>opener?.focus());
}
