import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename)

# lzma
import lzma
lzma.LZMAFile(filename)

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

# csv
import csv
with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# json
import json
with open(filename) as f:
    data = json.load(f)

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
conn = sqlite3.connect(
