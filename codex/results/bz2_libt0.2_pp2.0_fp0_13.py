import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename, mode='rt')

# lzma
import lzma
lzma.open(filename)

# tarfile
import tarfile
tar = tarfile.open(filename)
tar.extractall()
tar.close()

# zipfile
import zipfile
zip = zipfile.ZipFile(filename)
zip.extractall()
zip.close()

# pickle
import pickle
with open(filename, 'rb') as file:
    pickle.load(file)

# json
import json
with open(filename, 'r') as file:
    json.load(file)

# csv
import csv
with open(filename, 'r') as file:
    csv.reader(file, delimiter=',')

# xml
import xml.etree.ElementTree as ET
tree = ET.parse(filename)
root = tree.getroot()

# html
from bs4 import BeautifulSoup
with open(filename,
