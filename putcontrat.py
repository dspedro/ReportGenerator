import json

d={}
contrat="Raízen Energia"


d[aeronave]={
	"aeronave":aeronave,
	"prefixo":prefixo,
	"modelo":modelo,
	"tipo":tipo,
	"angulo":angulo,
	"faixa":faixa
}




with open("db/acft.json","w") as j:
	b=json.dumps(d)
	j.write(b)
#print(json.dumps(b))