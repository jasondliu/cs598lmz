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
tar = tarfile.open(path)
tar.getmembers()
tar.extractall()
tar.close()

# zipfile
import zipfile
zip = zipfile.ZipFile(path)
zip.namelist()
zip.extractall()
zip.close()

# pickle
import pickle
pickle.load(open(path, 'rb'))

# json
import json
json.load(open(path, 'r'))

# csv
import csv
f = open(path, 'r')
reader = csv.reader(f)
for line in reader:
    print(line)
f.close()

# xml
import xml.etree.ElementTree as ET
tree = ET.parse(path)
root = tree.getroot()

# html
from lxml
