import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename)

# lzma
import lzma
lzma.open(filename)

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
json.load(filename)

# pickle
import pickle
pickle.load(filename)

# shelve
import shelve
shelve.open(filename)

# struct
import struct
struct.pack(filename)

# xml
import xml.etree.ElementTree as ET
ET.parse(filename)

# html
import html.parser
html.parser.HTMLParser()

# sqlite3
import sqlite3
conn = sqlite3.connect(filename)

# ctypes
import ctypes
lib = ctypes.CDLL(filename)

# cffi
import cffi
ffi =
