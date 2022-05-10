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
pickle.dump(obj, open(filename, 'wb'))
pickle.load(open(filename, 'rb'))

# json
import json
json.dump(obj, open(filename, 'w'))
json.load(open(filename, 'r'))

# csv
import csv
csv.writer(open(filename, 'w'))
csv.reader(open(filename, 'r'))

# sqlite3
import sqlite3
conn = sqlite3.connect(filename)
cursor = conn.cursor()
cursor.execute('SELECT * FROM table')
cursor.fetchall()

# hdf5
import h5py

