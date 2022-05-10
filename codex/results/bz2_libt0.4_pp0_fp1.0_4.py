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
pickle.load(open(filename, 'rb'))

# json
import json
json.load(open(filename))

# csv
import csv
csv.reader(open(filename))

# xml
import xml.etree.ElementTree as etree
tree = etree.parse(filename)
root = tree.getroot()

# html
from lxml import html
tree = html.parse(filename)
root = tree.getroot()

# sqlite
import sqlite3
conn = sqlite3.connect(filename)
curs = conn.cursor()

# -----------------------------------------------------------------------------
# 10.3.2 通过网络
