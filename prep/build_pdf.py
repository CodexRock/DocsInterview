#!/usr/bin/env python3
"""Build the French preparation PDFs with local ReportLab and create a bookmarked bundle."""
from pathlib import Path
from xml.sax.saxutils import escape
import re, json, math
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak, KeepTogether
from reportlab.lib.enums import TA_LEFT
from pypdf import PdfReader, PdfWriter

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'pdf'; OUT.mkdir(exist_ok=True)
TEMP=ROOT.parent/'tmp'/'pdfs'; TEMP.mkdir(parents=True,exist_ok=True)
FONT=Path('/System/Library/Fonts/Supplemental')
for name,file in [('Prep','Arial.ttf'),('Prep-Bold','Arial Bold.ttf'),('Prep-Italic','Arial Italic.ttf'),('Prep-BoldItalic','Arial Bold Italic.ttf')]:
 pdfmetrics.registerFont(TTFont(name,str(FONT/file)))
pdfmetrics.registerFontFamily('Prep',normal='Prep',bold='Prep-Bold',italic='Prep-Italic',boldItalic='Prep-BoldItalic')
GREEN=colors.HexColor('#146347'); INK=colors.HexColor('#172D29'); GREY=colors.HexColor('#596962'); LIGHT=colors.HexColor('#EDF4EF')
W,H=A4; M=44; CW=W-2*M
styles={
 'body':ParagraphStyle('Body',fontName='Prep',fontSize=10.1,leading=14.4,spaceAfter=7,textColor=INK,allowWidows=0,allowOrphans=0),
 'h1':ParagraphStyle('H1',fontName='Prep-Bold',fontSize=24,leading=29,spaceAfter=14,textColor=GREEN,keepWithNext=True),
 'h2':ParagraphStyle('H2',fontName='Prep-Bold',fontSize=15,leading=19,spaceBefore=15,spaceAfter=8,textColor=GREEN,keepWithNext=True),
 'h3':ParagraphStyle('H3',fontName='Prep-Bold',fontSize=11.7,leading=16,spaceBefore=11,spaceAfter=6,textColor=INK,keepWithNext=True),
 'quote':ParagraphStyle('Quote',fontName='Prep',fontSize=10.4,leading=15.2,leftIndent=12,rightIndent=10,spaceBefore=5,spaceAfter=11,textColor=INK,backColor=LIGHT,borderPadding=9,allowWidows=0,allowOrphans=0),
 'bullet':ParagraphStyle('Bullet',fontName='Prep',fontSize=10.1,leading=14.4,leftIndent=13,firstLineIndent=0,spaceAfter=5,textColor=INK,bulletIndent=0,allowWidows=0,allowOrphans=0),
 'cell':ParagraphStyle('Cell',fontName='Prep',fontSize=8.4,leading=11.8,textColor=INK,spaceAfter=0,wordWrap='LTR'),
 'th':ParagraphStyle('TH',fontName='Prep-Bold',fontSize=8.4,leading=11.8,textColor=colors.white,spaceAfter=0),
 'small':ParagraphStyle('Small',fontName='Prep',fontSize=8.5,leading=12,textColor=GREY,spaceAfter=5),
}

def normalize(s):
 return s.replace('\u2011','-').replace('\u2013','-').replace('\u2014','-').replace('\u2212','-').replace('\u00a0',' ')

def inline(s):
 s=normalize(s)
 links=[]
 def link(m):
  links.append((m.group(1),m.group(2)))
  return f'ZZLINK{len(links)-1}ZZ'
 s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,s)
 s=escape(s)
 s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
 s=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<i>\1</i>',s)
 s=re.sub(r'`([^`]+)`',r'<font color="#4D625A">\1</font>',s)
 for i,(label,url) in enumerate(links):
  s=s.replace(f'ZZLINK{i}ZZ',f'<link href="{escape(url, {chr(34):"&quot;"})}" color="#146347"><u>{escape(label)}</u></link>')
 return s

class PrepDoc(SimpleDocTemplate):
 def afterFlowable(self,f):
  if isinstance(f,Paragraph) and f.style.name in ['H1','H2','H3']:
   level={'H1':0,'H2':1,'H3':2}[f.style.name]
   key=f'heading_{self.seq.nextf("heading")}'
   self.canv.bookmarkPage(key)
   self.canv.addOutlineEntry(f.getPlainText(),key,level=level,closed=level>0)

def footer(c,doc):
 c.saveState()
 c.setStrokeColor(colors.HexColor('#CCDAD0')); c.setLineWidth(.5)
 c.line(M,36,W-M,36)
 c.setFont('Prep',8); c.setFillColor(GREY)
 c.drawString(M,23,'Hamza Archane | Préparation BCG | 21 octobre 2026')
 c.drawRightString(W-M,23,str(doc.page))
 c.setFillColor(GREEN); c.rect(0,H-8,W,8,fill=1,stroke=0)
 c.restoreState()

def table(block):
 rows=[[c.strip() for c in line.strip().strip('|').split('|')] for line in block]
 rows=[r for r in rows if not all(re.fullmatch(r':?-+:?',c.replace(' ','')) for c in r)]
 n=len(rows[0]); rows=[r+['']*(n-len(r)) for r in rows]
 weights=[math.sqrt(max(8,min(45,max(len(r[j]) for r in rows)))) for j in range(n)]
 if n==6: weights=[1.6,1.0,1.0,1.0,1.0,1.6]
 widths=[CW*x/sum(weights) for x in weights]
 data=[[Paragraph(inline(c),styles['th' if i==0 else 'cell']) for c in r] for i,r in enumerate(rows)]
 t=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT',splitByRow=1)
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),GREEN),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.HexColor('#F1F5F2'),colors.white]),('LINEBELOW',(0,0),(-1,0),.5,GREEN),('LINEBELOW',(0,1),(-1,-1),.25,colors.HexColor('#D9E4DC'))]))
 return t

def parse(md, filename=''):
 lines=md.splitlines(); story=[]; i=0
 while i<len(lines):
  line=lines[i].strip()
  if not line: i+=1; continue
  if line.startswith('|'):
   block=[]
   while i<len(lines) and lines[i].strip().startswith('|'): block.append(lines[i]); i+=1
   t=table(block); t.spaceBefore=4; t.spaceAfter=10
   group=[t]
   if len(block)<=18 and story and isinstance(story[-1],Paragraph) and story[-1].style.name in ['H2','H3']:
    group.insert(0,story.pop())
   story.append(KeepTogether(group) if len(block)<=18 else t); continue
  if line=='---':
   story.extend([Spacer(1,8),HRFlowable(width='100%',thickness=.5,color=colors.HexColor('#B9D0C0')),Spacer(1,5)]); i+=1;continue
  m=re.match(r'^(#{1,3})\s+(.*)',line)
  if m:
   level=len(m.group(1)); heading=m.group(2)
   if (filename.startswith('06_') and re.match(r'C[0-9]+ -',heading)) or heading.startswith('Fiche de révision -') or (filename.startswith('04_') and heading.startswith('9. Les finances')):
    if story and isinstance(story[-1],Spacer): story.pop()
    story.append(PageBreak())
   story.append(Paragraph(inline(heading),styles[f'h{level}']))
   if level==1: story.append(Paragraph('DOSSIER PERSONNEL DE PRÉPARATION - VERSION DU 15 OCTOBRE 2026 - NON OFFICIEL',styles['small']))
   i+=1;continue
  if line.startswith('>'):
   block=[]
   while i<len(lines) and lines[i].strip().startswith('>'):
    block.append(lines[i].strip()[1:].strip());i+=1
   text=' '.join(block);text=re.sub(r'\s+',' ',text)
   story.append(Paragraph(inline(text),styles['quote']));continue
  if line.startswith('- '):
   story.append(Paragraph(inline(line[2:]),styles['bullet'],bulletText='•'));i+=1;continue
  block=[line];i+=1
  while i<len(lines) and lines[i].strip() and not re.match(r'^(#{1,3}\s|\||>|- |---$)',lines[i].strip()):
   block.append(lines[i].strip());i+=1
  paragraph=' '.join(block)
  body_style=styles['body']
  if paragraph.startswith('**Scénario fictif.**'):
   body_style=ParagraphStyle('ScenarioIntro',parent=styles['body'],keepWithNext=True)
  story.append(Paragraph(inline(paragraph),body_style))
 if filename.startswith('02_') or filename.startswith('05_'):
  grouped=[]; chunk=[]
  for f in story:
   if isinstance(f,Paragraph) and f.style.name=='H2':
    if chunk: grouped.append(KeepTogether(chunk)); chunk=[]
    title=f.getPlainText()
    should_group=(filename.startswith('02_') and (re.match(r'C[0-9]+ -',title) or title.startswith('5. Réagir'))) or (filename.startswith('05_') and re.match(r'(Jeudi|Vendredi|Samedi|Dimanche|Lundi|Mardi) ',title))
    if should_group: chunk=[f]; continue
   if chunk: chunk.append(f)
   else: grouped.append(f)
  if chunk: grouped.append(KeepTogether(chunk))
  story=grouped
 return story

def build_one(path):
 dst=OUT/(path.stem+'.pdf')
 doc=PrepDoc(str(dst),pagesize=A4,rightMargin=M,leftMargin=M,topMargin=36,bottomMargin=49,title=path.read_text().splitlines()[0].lstrip('# '),author='Dossier personnel Hamza Archane',pageCompression=1)
 body_before=(styles['body'].leading,styles['body'].spaceAfter)
 if path.name.startswith('07_'):
  styles['body'].leading=14.0; styles['body'].spaceAfter=6
 doc.build(parse(path.read_text(),path.name),onFirstPage=footer,onLaterPages=footer)
 styles['body'].leading,styles['body'].spaceAfter=body_before
 return dst

files=[build_one(p) for p in sorted(ROOT.glob('0[0-7]_*.md'))]
counts=[len(PdfReader(p).pages) for p in files]
# Two-page front matter gives a stable, printed index to the combined file.
cover=[Spacer(1,70),Paragraph('BCG<br/>ERP Digital Strategy',styles['h1']),Spacer(1,15),Paragraph('Hamza Archane',styles['h2']),Paragraph('Entretien du mercredi 21 octobre 2026<br/>11h00-11h30 | Paris | Zoom | Français',styles['body']),Spacer(1,25),Paragraph('Un parcours clair. Des preuves précises.<br/>Des décisions qui tiennent dans l’exécution.',styles['h2']),Spacer(1,25),Paragraph('Dossier personnel, non officiel. Cas et scénarios de répétition fictifs. Les questions exactes et le résultat de recrutement ne sont pas connus.',styles['body']),Paragraph('Version enrichie et sourcée du 15 octobre 2026. Commencer par le guide 00, puis utiliser le plan de trois heures par jour. Le guide 06 contient les corrigés : le garder fermé avant la pratique.',styles['body']),PageBreak(),Paragraph('Sommaire du dossier',styles['h1']),Paragraph('Pagination du PDF complet. Les pages des fascicules ont aussi leur propre numéro en pied de page. Les signets permettent de naviguer par document et section.',styles['body'])]
start=3; index=[]
for p,n in zip(files,counts):
 title=PdfReader(p).metadata.title
 index.append([title,str(start)])
 start+=n
cover.append(table(['| Document | Page du PDF complet |','|---|---|']+['| '+a+' | '+b+' |' for a,b in index]))
cover.extend([Spacer(1,14),Paragraph('Parcours conseillé',styles['h2']),Paragraph('Aujourd’hui : guide 00, pitch et motivation, cas C1 avec partenaire. Chaque jour : pratique orale, calculs et reprise des erreurs. Conserver trois cas inédits pour les simulations du 18, 19 et 20 octobre.',styles['body']),Paragraph('Les sources, leurs limites et les corrections du premier pack figurent dans le document 07. Les expériences non documentées ne deviennent pas vérifiées parce qu’un scénario est plausible.',styles['body'])])
front=TEMP/'front_matter.pdf'
PrepDoc(str(front),pagesize=A4,leftMargin=M,rightMargin=M,topMargin=36,bottomMargin=49,title='Sommaire',author='Hamza Archane').build(cover,onFirstPage=footer,onLaterPages=footer)
assert len(PdfReader(front).pages)==2,'Front matter size changed; regenerate index.'
writer=PdfWriter(); writer.append(str(front),outline_item='Dossier et sommaire',import_outline=False)
for p in files: writer.append(str(p),outline_item=PdfReader(p).metadata.title,import_outline=True)
writer.add_metadata({'/Title':'BCG - Dossier complet de préparation - Hamza Archane','/Author':'Dossier personnel Hamza Archane','/Subject':'ERP Digital Strategy | 21 octobre 2026 | version enrichie'})
with (OUT/'08_Dossier_Complet_BCG_Hamza.pdf').open('wb') as f:writer.write(f)
manifest=[{'file':str(p.relative_to(ROOT.parent)),'pages':n} for p,n in zip(files,counts)]
manifest.append({'file':'prep/pdf/08_Dossier_Complet_BCG_Hamza.pdf','pages':2+sum(counts)})
(TEMP/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print(json.dumps(manifest,ensure_ascii=False,indent=2))
