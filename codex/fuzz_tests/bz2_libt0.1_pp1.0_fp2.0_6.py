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
pickle.load(file)

# json
import json
json.load(file)

# csv
import csv
csv.reader(file)

# xml
import xml.etree.ElementTree as et
tree = et.parse(filename)
root = tree.getroot()

# html
from lxml import html
tree = html.parse(filename)
root = tree.getroot()

# sqlite3
import sqlite3
conn = sqlite3.connect(filename)
curs = conn.cursor()

# pandas
import pandas
df = pandas.read_csv(filename)

# xlrd
import xlrd
wb
