import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename, mode='rt')

# lzma
import lzma
lzma.open(filename)

# zipfile
import zipfile
zipfile.ZipFile(filename)

# tarfile
import tarfile
tarfile.open(filename)

# pickle
import pickle
pickle.load(file)

# json
import json
json.load(file)

# csv
import csv
csv.reader(file)

# xml
import xml.etree.ElementTree as etree
tree = etree.parse(filename)
root = tree.getroot()

# sqlite3
import sqlite3
conn = sqlite3.connect(filename)
curs = conn.cursor()
curs.execute(query)
curs.fetchall()

# lxml
import lxml.etree as etree
tree = etree.parse(filename)
root = tree.getroot()

# requests
import requests
r =
