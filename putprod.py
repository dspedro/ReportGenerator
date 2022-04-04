import json

d={}
produto="Moddus Maturador"
nome="Moddus"
fromulacao="EC"
dosemax="1,2"
dosemin="0,8"
caldamax="40"
caldamin="30"
classe="III"
tempmax="30"
tempmin="5"
umidmin="60"
umidmax="99"
ventomax="10"
ventomin="3"


d[produto]={
	"nome":nome,
	"fromulacao":fromulacao,
	"dosemax":dosemax,
	"dosemin":dosemin,
	"caldamax":caldamax,
	"caldamin":caldamin,
	"classe":classe,
	"tempmax":tempmax,
	"tempmin":tempmin,
	"umidmin":umidmin,
	"umidmax":umidmax,
	"ventomax":ventomax,
	"ventomin":ventomin	
}




with open("db/produto.json","w") as j:
	b=json.dumps(d)
	j.write(b)
#print(json.dumps(b))