import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename)

# lzma
import lzma
lzma.open(filename)

# tar
import tarfile
tar = tarfile.open(filename)
tar.extractall()
tar.close()

# zip
import zipfile
zip = zipfile.ZipFile(filename)
zip.extractall()
zip.close()

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
import xml.etree.ElementTree as et
tree = et.parse(filename)
root = tree.getroot()

# html
from lxml import html
tree = html.parse(filename)
root = tree.getroot()

# sqlite
import sqlite3
conn = sqlite3.connect(filename)
c = conn.cursor()
c.execute
