import bz2
bz2.BZ2File(filename).read()

# gzip
import gzip
gzip.open(filename, 'rt').read()

# lzma
import lzma
lzma.open(filename).read()

# zipfile
import zipfile
zipfile.ZipFile(filename).read(filename)

# tarfile
import tarfile
tarfile.open(filename).extractall(path='.')

# pickle
import pickle
pickle.load(filename)

# JSON
import json
json.load(filename)

# CSV
import csv
csv.reader(filename)

# XML
import xml.etree.ElementTree as etree
tree = etree.parse(filename)
root = tree.getroot()

# HTML
from lxml import html
tree = html.parse(filename)
root = tree.getroot()

# Binary Data
import struct
struct.unpack(fmt, data)

# Image
from PIL import Image
Image.open(filename)

# Audio
from PIL import Image

