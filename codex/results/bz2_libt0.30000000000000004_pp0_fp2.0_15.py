import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename)

# lzma
import lzma
lzma.LZMAFile(filename)

# zip
import zipfile
zipfile.ZipFile(filename)

# tar
import tarfile
tarfile.TarFile(filename)

# pickle
import pickle
pickle.load(filename)

# json
import json
json.load(filename)

# csv
import csv
csv.reader(filename)

# xml
import xml.etree.ElementTree as etree
tree = etree.parse(filename)

# html
import html.parser
p = html.parser.HTMLParser()
p.feed(filename)

# sqlite3
import sqlite3
conn = sqlite3.connect(filename)

# mmap
import mmap
f = open(filename, 'r+')
m = mmap.mmap(f.fileno(), 0)

# struct
import struct
struct.unpack(filename)

