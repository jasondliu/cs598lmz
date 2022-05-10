import bz2
bz2.open('/home/felipe/Documents/data/projeto/general/dados/empresas_abertas/empresas_abertas_201906.xml.bz2')

import urllib, json

url = 'https://dadosabertos.camara.leg.br/api/v2/proposicoes?ordem=ASC&ordenarPor=ano'

response = urllib.request.urlopen(url)
data = json.loads(response.read())
print(json.dumps(data, indent=4, sort_keys=True))

# Proposições
import bz2
bz2.open('/home/felipe/Documents/data/projeto/general/dados/proposicoes/proposicoes_201906.xml.bz2')

import urllib, json

url = 'https://dadosabertos.camara.leg.br/api/v2/proposicoes?ordem=ASC&ordenarPor=
