import mmap
import re

config = Settings()

try:
	import pymongo
	from pymongo import MongoClient as Connection
except ImportError:
	logging.error("You need to install pymongo for this script: http://api.mongodb.org/python/current/installation.html")
	sys.exit(1)

def connect():
	connection = Connection(config.mongo_host, config.mongo_port)
	db = connection[config.mongo_database]
	if config.mongo_user and config.mongo_pass:
		db.authenticate(config.mongo_user, config.mongo_pass)
	return db

def find_seeds():
	db = connect()
	s = db.torrents.find({"seeds": {"$gt": 60}})
	for _ in s:
		print _["torrent_name"]

def find_torrents(name):
	db = connect()
	s = db.torrents.find({"torrent_name": re.compile
