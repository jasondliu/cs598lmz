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
tarfile.open(filename)

# zip
import zipfile
zipfile.ZipFile(filename)

# csv
import csv
csv.reader(open(filename))

# json
import json
json.load(open(filename))

# xml
import xml.etree.ElementTree as etree
etree.parse(filename)

# yaml
import yaml
yaml.load(open(filename))

# pickle
import pickle
pickle.load(open(filename))

# shelve
import shelve
shelve.open(filename)

# sqlite3
import sqlite3
conn = sqlite3.connect(filename)

# csv
import csv
csv.reader(open(filename))

# json
import json
json.load(open(filename))

# xml
