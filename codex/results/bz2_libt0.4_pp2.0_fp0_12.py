import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename)

# lzma
import lzma
lzma.LZMAFile(filename)

# zipfile
import zipfile
zipfile.ZipFile(filename)

# tarfile
import tarfile
tarfile.open(filename)

# csv
import csv
csv.reader(filename)

# json
import json
json.loads(filename)

# xml
import xml.etree.ElementTree as ET
ET.parse(filename)

# yaml
import yaml
yaml.load(filename)

# pickle
import pickle
pickle.load(filename)

# shelve
import shelve
shelve.open(filename)

# hdf5
import h5py
h5py.File(filename)

# sqlite3
import sqlite3
conn = sqlite3.connect(filename)

# sqlalchemy
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///
