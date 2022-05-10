import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename)

# lzma
import lzma
lzma.open(filename)

# zip
import zipfile
zipfile.ZipFile(filename)

# tar
import tarfile
tarfile.open(filename)

# pickle
import pickle
pickle.load(filename)

# json
import json
json.load(filename)

# csv
import csv
csv.reader(filename)

# xml
import xml.etree.ElementTree as et
tree = et.parse(filename)
root = tree.getroot()

# html
import lxml.html
tree = lxml.html.parse(filename)
root = tree.getroot()

# sqlite
import sqlite3
conn = sqlite3.connect(filename)
cursor = conn.cursor()
cursor.execute('select * from table')
cursor.fetchall()

# excel
import openpyxl
wb = openpyxl.load
