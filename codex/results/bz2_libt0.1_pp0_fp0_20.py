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
tree = et.parse(file)
root = tree.getroot()

# sqlite3
import sqlite3
conn = sqlite3.connect(filename)
curs = conn.cursor()
curs.execute(query)
curs.fetchall()

# pandas
import pandas as pd
pd.read_csv(filename)
pd.read_excel(filename)
pd.read_sql(query, conn)
pd.
