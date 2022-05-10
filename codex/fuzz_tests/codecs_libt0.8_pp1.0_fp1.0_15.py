import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'utf8mb4' else None)
import torndb
import pymongo
from bson import json_util
from bson.objectid import ObjectId
import configparser
import time

class DBMongo:
    def __init__(self, host='localhost', port=27017, config_file=config_file, connect=False):
        self.host = host
        self.port = port
        self.config_file = config_file
        self.db_mongo = None

        if connect:
            self.connect()

    def connect(self):
        if self.db_mongo is None:
            try:
                self.db_mongo = pymongo.MongoClient(self.host, self.port)
            except:
                print("Failed to connect to DB server.")
                self.db_mongo = None

    def read_document(self, dbname, colname, filterparam):
        if self.db_mongo is None:
            self.connect
