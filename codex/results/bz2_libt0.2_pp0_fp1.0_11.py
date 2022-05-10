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

# xlrd
import xlrd
xlrd.open_workbook(filename)

# sqlite3
import sqlite3
conn = sqlite3.connect(filename)

# hdf5
import h5py
h5py.File(filename)

# BeautifulSoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

# lxml
from lxml import etree
tree = etree.parse(filename)

# pyquery
