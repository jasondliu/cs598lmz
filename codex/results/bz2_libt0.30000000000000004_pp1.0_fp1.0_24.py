import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename, mode='rb')

# lzma
import lzma
lzma.open(filename)

# zipfile
import zipfile
zipfile.ZipFile(filename)

# tarfile
import tarfile
tarfile.open(filename)

# csv
import csv
csv.reader(open(filename))

# json
import json
json.load(open(filename))

# xml
import xml.etree.ElementTree as ET
tree = ET.parse(filename)
root = tree.getroot()

# html
from lxml import html
tree = html.parse(filename)

# sqlite
import sqlite3
conn = sqlite3.connect(filename)
curs = conn.cursor()

# mongodb
import pymongo
conn = pymongo.MongoClient()
db = conn.database
collection = db.collection

# redis
import redis
conn = redis.Redis()

#
