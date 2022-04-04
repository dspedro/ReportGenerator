
import json
import jmespath
import webbrowser

def html (inc,dic):
  numero = 1 # um numero para a variavel da html
  n2 = 1 # incremental de aeronave
  n3 = 1
  db = open("db/r/"+str(inc)+".json","r")
  dbj = json.load(db)
  #print(dbj)
  dbA = open('db/acft.json','r')
  dba = json.load(dbA)

  dbP = open('db/produto.json','r')
  dbp = json.load(dbP)

  dbL = open('db/pista.json','r')
  dbl = json.load(dbL)

  f = open("html/"+str(inc)+".html","w")
  with open('report1.html') as file:
    ht = str(file.read())
  #ht = ht.replace("00000-0","12354")
  #ht = ht.replace("a1",str(dbj[str(inc)]['contratante']))

  for elemento in dbp[str(dbj[str(inc)]['produto'])]:
    ht = ht.replace(str("p"+str(n3)),str(dbp[str(dbj[str(inc)]['produto'])][elemento]),1)
    n3 +=1

  for elemento in dba[str(dbj[str(inc)]['aeronave'])]:
    ht = ht.replace(str("s"+str(n2)),str(dba[str(dbj[str(inc)]['aeronave'])][elemento]),1)
    n2 += 1

  for elemento in dbj[str(inc)]:
    print(dbj[str(inc)][elemento])
    ht = ht.replace(str("a"+str(numero)),str(dbj[str(inc)][elemento]),1)
    numero += 1
  ht = ht.replace('$numero', str(inc))
  ht = ht.replace('a31',str(dbj[str(inc)]['dataassin']))
  ht = ht.replace('liquido','')
  ht = ht.replace('solido','')
  ht = ht.replace('$pista',str(dbl[str(dbj[str(inc)]['pista'])]['coordenada']))


  f.write(ht)
  f.close()

  webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files (x86)/Google/Chrome/Application/chrome.exe"))
  webbrowser.get('chrome').open('html/'+str(inc)+'.html')
#html(5,0)
		