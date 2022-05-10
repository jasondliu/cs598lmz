import bz2
bz2.BZ2File(filename, 'r')

# gzip
import gzip
gzip.GzipFile(filename, 'r')

# lzma
import lzma
lzma.LZMAFile(filename, 'r')

# zip
import zipfile
zipfile.ZipFile(filename, 'r')

# tar
import tarfile
tarfile.TarFile(filename, 'r')

# csv
import csv
csv.reader(open(filename, 'r'))

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
root = tree.getroot()

# sqlite
import sqlite3
conn = sqlite3.connect(filename)
curs = conn.cursor()
curs.execute('select * from table')
curs.fetchall()

# hdf5
import h5
