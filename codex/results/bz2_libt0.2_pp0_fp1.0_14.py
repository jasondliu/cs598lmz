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

# yaml
import yaml
yaml.load(open(filename))

# csv
import csv
csv.reader(open(filename))

# xml
import xml.etree.ElementTree as etree
etree.parse(filename)

# html
import lxml.html
lxml.html.parse(filename)

# sqlite3
import sqlite3
conn = sqlite3.connect(filename)

# pandas
import pandas
pandas.read_csv(filename)

# matplotlib
import mat
