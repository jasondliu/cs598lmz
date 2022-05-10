import bz2
bz2.BZ2File(filename).read()

# gzip
import gzip
gzip.open(filename).read()

# zip
from zipfile import ZipFile
z = ZipFile(filename)
z.read('spam.txt')

# tar
from tarfile import TarFile
t = TarFile(filename)
t.read('spam.txt')

# pickle
import pickle
pickle.load(open(filename))

# shelve
import shelve
s = shelve.open(filename)
s['key']
s.close()

# CSV
import csv
csv.reader(open(filename))

# XML
import xml.etree.ElementTree as et
et.parse(filename)

# HTML
from HTMLParser import HTMLParser
p = HTMLParser()
p.parse(open(filename))

# JSON
import json
json.load(open(filename))

# SQL
import sqlite3
conn = sqlite3.connect(filename)
curs = conn.cursor()
curs.execute('select * from table
