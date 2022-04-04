import json

d={}
aeronave="PTBYR Liquido"
prefixo="PTBYR"
modelo="Bico hidraulico"
tipo="CP"
angulo="135"
faixa="24"

d[aeronave]={
	"aeronave":aeronave,
	"prefixo":prefixo,
	"modelo":modelo,
	"tipo":tipo,
	"angulo":angulo,
	"faixa":faixa
}

with open("db/acft.json") as f:
	data=json.load(f)

#for name in data:
#	print(name)

data.update(d)

#print(data)

with open("db/acft.json","w") as a:
	a.write(json.dumps(data))