import bz2
bz2.BZ2File(filepath)

# gzip
import gzip
gzip.open(filepath, 'rt')

# lzma
import lzma
lzma.open(filepath)

# zipfile
import zipfile
with zipfile.ZipFile(filepath) as zf:
    print(zf.namelist())

# tarfile
import tarfile
with tarfile.open(filepath) as tf:
    print(tf.getnames())

# pickle
import pickle
with open(filepath, 'rb') as f:
    pickle.load(f)

# json
import json
with open(filepath, 'r') as f:
    json.load(f)

# csv
import csv
with open(filepath, 'r') as f:
    csv.reader(f)

# xml
import xml.etree.ElementTree as et
tree = et.parse(filepath)
root = tree.getroot()

# html
from lxml import html
with open(filepath
