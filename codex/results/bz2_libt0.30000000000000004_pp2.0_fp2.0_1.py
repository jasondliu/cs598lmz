import bz2
bz2.BZ2File(path, 'r')

# gzip
import gzip
gzip.open(path, 'rt')

# lzma
import lzma
lzma.open(path)

# zip
import zipfile
zf = zipfile.ZipFile(path)
zf.open('somefile.txt')

# tar
import tarfile
tf = tarfile.open(path)
tf.extractall(path='/tmp/some/new/folders')
tf.close()

# csv
import csv
f = open(path, 'r')
reader = csv.reader(f)
for line in reader:
    print(line)

# json
import json
json.load(f)

# xml
from xml.etree.ElementTree import parse
doc = parse(path)

# html
from lxml.html import parse
doc = parse(path)
doc.find('.//title').text

# binary data
import struct
with open(path, 'rb') as f:
    data = f
