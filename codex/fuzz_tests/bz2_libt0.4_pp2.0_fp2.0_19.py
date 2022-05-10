import bz2
bz2.BZ2File(filename).read()

# gzip
import gzip
gzip.open(filename, 'rt').read()

# lzma
import lzma
lzma.open(filename).read()

# tar
import tarfile
with tarfile.open(filename) as f:
    f.extractall()

# zip
import zipfile
with zipfile.open(filename) as f:
    f.extractall()

# json
import json
json.dumps([1, 'simple', 'list'])
json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')

# xml
import xml.etree.ElementTree as et
tree = et.parse(filename)
root = tree.getroot()

# csv
import csv
with open(filename) as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Process row
        pass

# sqlite
import sqlite
