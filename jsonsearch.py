import json
import jmespath

file=open("db/produto.json")
data=json.load(file)

acft="PTBYP"

src="ModdusMaturador.formulacao"

print(jmespath.search(src,data))