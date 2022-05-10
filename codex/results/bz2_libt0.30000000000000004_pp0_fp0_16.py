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

# csv
import csv
csv.reader(filename)

# json
import json
json.load(filename)

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

# pandas
import pandas as pd
pd.read_csv(filename)
pd.read_excel(filename)
pd.read_sql(query, conn)
pd.read_json(
