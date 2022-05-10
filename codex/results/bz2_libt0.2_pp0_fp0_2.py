import bz2
bz2.BZ2File('data/example.bz2').read()

# gzip
import gzip
gzip.open('data/example.gz').read()

# lzma
import lzma
lzma.open('data/example.xz').read()

# zip
import zipfile
zipfile.ZipFile('data/example.zip').read('README.txt')

# tar
import tarfile
tarfile.open('data/example.tar.gz').read()

# pickle
import pickle
pickle.loads(b'\x80\x03]q\x00(X\x01\x00\x00\x00aq\x01X\x01\x00\x00\x00bq\x02e.')

# json
import json
json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')

# xml
import xml.etree.ElementTree as ET
tree = ET.parse('data/example.xml')
root = tree.getroot()
root.
