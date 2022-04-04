import json

n2 = 1 # incremental de aeronave
db = open("db/r/"+str(13)+".json","r")
dbj = json.load(db)
#print(dbj)
dbA = open('db/acft.json','r')
dba = json.load(dbA)

print(str(dbj[str(13)]['aeronave']))
#for elemento in dba[str(db[str(15)]['aeronave']