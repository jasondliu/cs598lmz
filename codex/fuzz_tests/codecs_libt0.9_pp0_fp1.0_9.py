import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
import random
import json

#server = "mongodb://45.79.171.67:27017"
server = "mongodb://127.0.0.1:27017"

client = MongoClient(server)
db = client.redditByArtist

count = 0
#for artist in db.russianEmpire.find({}):
#	count += 1
for artist in db.violetLucas.find({}, no_cursor_timeout=True):
	print(count)
	count += 1

	artists = ['mattiavettorello', 'BarbarianKing', 'VioletLucas', 'DirkVonLowtzow', 
				'feharts', 'SergioCantu', 'ShipengChen', 'ScottVallas', 'Toru_Sanogawa', 'MerkvilsonSaca',
				'DevrimKahraman', 'BrendonHuor', 'Rahll',
