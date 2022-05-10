import mmap
from pymongo import MongoClient
from bson.objectid import ObjectId
import configparser
import json
from datetime import datetime
from datetime import timedelta
import time
import os

# Get the config file
config = configparser.ConfigParser()
config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.ini'))

# Connect to MongoDB
client = MongoClient('mongodb://' + config['DEFAULT']['MongoDB_Host'] + ':' + config['DEFAULT']['MongoDB_Port'])
db = client[config['DEFAULT']['MongoDB_Database']]
collection = db[config['DEFAULT']['MongoDB_Collection']]

# Open the log file
f = open("/var/log/apache2/access.log","r+b")

# Find the size of the file and move to the end
st_results = os.stat("/var/log/apache2/access.log")
st_size = st_
