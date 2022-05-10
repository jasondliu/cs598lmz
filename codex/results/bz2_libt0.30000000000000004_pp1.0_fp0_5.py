import bz2
bz2.BZ2File(filename)

import gzip
gzip.open(filename)

import lzma
lzma.LZMAFile(filename)

import zipfile
zipfile.ZipFile(filename)

import tarfile
tarfile.open(filename)

# Reading Binary Data
with open('somefile.bin', 'rb') as f:
    data = f.read()

# Writing Text Data
with open('somefile.txt', 'wt') as f:
    f.write(text)

# Writing Binary Data
with open('somefile.bin', 'wb') as f:
    f.write(b'Hello World')

# Saving Structured Data with json
import json
data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}
json_str = json.dumps(data)

data = json.loads(json_str)

# Saving Structured Data with pickle
import pickle
data = {
    'name': 'ACME',
    'sh
