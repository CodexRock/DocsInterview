#!/usr/bin/env python3
from pathlib import Path
from datetime import date
from zoneinfo import ZoneInfo
from datetime import datetime
import json, math, re
from pypdf import PdfReader
import pdfplumber
ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,value,expected,tol=1e-6):
 ok=math.isclose(value,expected,abs_tol=tol,rel_tol=tol)
 checks.append({'check':name,'actual':value,'expected':expected,'passed':ok})
 assert ok,name
check('C1 team cost',40*.06,2.4)
check('C1 capacity ETP',20*.8+20*.5,26)
check('C1 capacity hours',26*1600,41600)
check('C1 cash labor',10*.06,.6)
check('C1 extra discounts',100*.02*(.6-.2),.8)
check('C1 year 1',(.6+.8)*.5-.4,.3)
check('C1 cash payback months',(2+(1.5-.3-1)/1)*12,26.4)
check('C1 from build months',26.4+3,29.4)
check('C1 3yr cash',-1.5+.3+1+1,.8)
check('C1 threshold upfront at 24mo',.3+1,1.3)
check('C1 required price reduction',.2/1.5,2/15)
check('C1 full capture payback months',(1+(1.5-((1.56+.8)*.5-.4))/(1.56+.8-.4))*12,16.4081632653)
check('C1 no discount payback',1+(1.5-(-.1))/.2,9)
check('C2 option A',-18+1+7+9+3,2)
check('C2 option B',-30+0+12+18+8,8)
check('C2 option C',-20+4+10+12+5,11)
check('C2 payback C months',(2+1/12)*12,25)
check('C2 payback A months',(2+7/9)*12,33.33333333)
check('C2 C stress',-20+.7*(4+10+12)+5,3.2)
check('C3 complete',54-40,14)
check('C3 reduced',45-24,21)
check('C3 critical test rate',15/20,.75)
check('C4 D cash',3*13-12,27)
check('C4 E cash',18+28-45,1)
check('C4 D annual total',122+13,135)
check('C4 residual target',150-135,15)
check('C5 recovery',5000*.8+4000*.75+3000*.8,9400)
check('C5 resulting OTIF',(84000+9400)/100000,.934)
check('C5 remaining orders',94000-93400,600)
check('C6 initial result',80000*40+20000*100-2e6,3.2e6)
check('C6 new result',100000*40+10000*100-2.4e6,2.6e6)
check('C6 new price result',96000*45+10000*100-2.4e6,2.92e6)
check('C6 max volume drop',1-(4e6/45)/100000,1/9)
check('C6 extra B units',.28e6/100,2800)
check('C7 build',-1.2+2*(1-.2),.4)
check('C7 buy',-.25+2.75*(1-.45),1.2625)
check('C7 buy payback months',(.25+.25/.55)*12,8.4545454545)
check('C8 large volume',2000*.7*1200*12,20.16e6)
check('C8 medium volume',8000*.5*300*12,14.4e6)
check('C8 TAM',34.56e6*.2,6.912e6)
check('C8 SAM',34.56e6*.6*.2,4.1472e6)
check('C8 SOM volume',34.56e6*.6*.15,3.1104e6)
check('C8 annual result',3.1104e6*.15-.8e6,-.33344e6)
check('C8 threshold volume share',(.8e6/.15)/(34.56e6*.6),.2572016461)
check('Drill DSO',730e6/365*5,10e6)
check('Drill DIO',365e6/365*4,4e6)
check('Drill CAGR',(121/100)**.5-1,.1)
check('Drill growth',100*1.1*1.1*.9,108.9)
check('Drill NPV',-100+66/1.1+72.6/(1.1**2),20)
assert date(2026,10,21).weekday()==2
assert datetime(2026,10,21,11,tzinfo=ZoneInfo('Europe/Paris')).utcoffset().total_seconds()==7200
text=(ROOT/'05_Cheat_Sheet_et_Conseils.md').read_text()
for sec in [s for s in re.split(r'^## ',text,flags=re.M) if re.match(r'(Jeudi|Vendredi|Samedi|Dimanche|Lundi|Mardi) ',s)]:
 times=[int(n) for n in re.findall(r'^- \*\*(\d+) min',sec,flags=re.M)]
 assert sum(times)==180,(sec[:50],times)
files=sorted((ROOT/'pdf').glob('0[0-7]_*.pdf'))
assert len(files)==8
manifest=[]; edge_issues=[]
for p in files:
 r=PdfReader(p); page_text=[x.extract_text() for x in r.pages]
 assert all(len(t.strip())>100 for t in page_text),p.name
 assert r.outline,p.name
 assert '\u25a0' not in ''.join(page_text),p.name
 with pdfplumber.open(p) as pdf:
  for i,page in enumerate(pdf.pages,1):
   for ch in page.chars:
    if ch['text'].strip() and (ch['x0']<40 or ch['x1']>page.width-40 or ch['top']<15 or ch['bottom']>page.height-15):
     edge_issues.append((p.name,i,ch['text'],[round(ch[k],1) for k in ['x0','x1','top','bottom']]))
 manifest.append({'file':p.name,'pages':len(r.pages),'links':sum(len(p.get('/Annots',[])) for p in r.pages)})
assert not edge_issues,edge_issues[:10]
master=PdfReader(ROOT/'pdf/08_Dossier_Complet_BCG_Hamza.pdf')
assert len(master.pages)==sum(x['pages'] for x in manifest)+2
report={'arithmetic_checks':len(checks),'all_arithmetic_passed':True,'daily_minutes':180,'interview_paris_offset_hours':2,'pdfs':manifest,'master_pages':len(master.pages),'edge_issues':edge_issues,'checks':checks}
(ROOT/'research/validation_report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps({k:v for k,v in report.items() if k!='checks'},ensure_ascii=False,indent=2))
