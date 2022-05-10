import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename, mode='rb')

# lzma
import lzma
lzma.open(filename)

# tar
import tarfile
tar = tarfile.open(filename)

# zip
import zipfile
zf = zipfile.ZipFile(filename)

# csv
import csv
with open(filename, 'r', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# json
import json
with open(filename, 'r') as f:
    obj = json.load(f)

# xml
import xml.etree.ElementTree as et
tree = et.parse(filename)
root = tree.getroot()

# html
from bs4 import BeautifulSoup
with open(filename, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# sqlite
import sqlite
