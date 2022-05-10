import bz2
bz2.BZ2File(filename)

import gzip
gzip.open(filename, mode='rt')

import lzma
lzma.open(filename)

import zipfile
zf = zipfile.ZipFile(filename)
zf.open(zf.namelist()[0])

import tarfile
tf = tarfile.open(filename)
tf.extractfile(tf.getnames()[0])

import csv
f = open(filename)
csv.reader(f)

import json
json.load(open(filename))

import xml.etree.ElementTree as et
tree = et.parse(filename)
root = tree.getroot()

import email
message = email.message_from_file(open(filename))

import html
html.parse(filename)

import sqlite3
conn = sqlite3.connect(filename)
curs = conn.cursor()
curs.execute('select * from table')

import lxml.html
tree = lxml.html.parse(filename)

import cssutils
