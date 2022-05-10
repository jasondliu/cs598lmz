import bz2
bz2.BZ2File(path).read()

# gzip
import gzip
gzip.open(path).read()

# lzma
import lzma
lzma.open(path).read()

# tarfile
import tarfile
tarfile.open(path).read()

# zipfile
import zipfile
zipfile.ZipFile(path).read()

# csv
import csv
csv.reader(open(path))

# json
import json
json.load(open(path))

# yaml
import yaml
yaml.load(open(path))

# xml
import xml.etree.ElementTree as ET
ET.parse(path)

# html
from lxml import html
tree = html.parse(path)

# sqlite
import sqlite3
conn = sqlite3.connect(path)

# excel
import xlrd
book = xlrd.open_workbook(path)

# hdf5
import h5py
h5 = h5py.File(path)

# mat
