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
zf = zipfile.ZipFile(filename)
zf.namelist()
zf.read(zf.namelist()[0])

# tarfile
import tarfile
tf = tarfile.open(filename)
tf.getnames()
tf.extractfile(tf.getnames()[0]).read()

# pickle
import pickle
pickle.load(open(filename, 'rb'))

# json
import json
json.load(open(filename, 'r'))

# csv
import csv
f = open(filename, 'r')
csv_f = csv.reader(f)
for row in csv_f:
    print(row)

# xml
import xml.etree.ElementTree as ET
tree = ET.parse(filename)
root = tree.getroot()
