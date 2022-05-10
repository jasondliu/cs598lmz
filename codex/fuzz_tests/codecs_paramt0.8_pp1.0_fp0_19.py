import codecs
codecs.register_error('strict', codecs.ignore_errors)

from pymongo import MongoClient
from pymongo import GEOSPHERE as GEO

def create_indexes(db):
	db['tweets'].create_index([('location', GEO)], background=True)

def main(config):
	client = MongoClient(config['MONGO_HOST'], config['MONGO_PORT'])
	db = client['twitris']
	
	create_indexes(db)


if __name__ == '__main__':
	import json
	f = open('config.json')
	config = json.load(f)
	f.close()

	for key in config:
		os.environ[key] = config[key]
	
	main(config)
