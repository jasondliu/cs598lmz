import bz2
bz2.BZ2File(path).read()

# gzip
import gzip
gzip.open(path).read()

# lzma
import lzma
lzma.open(path).read()

# tar
import tarfile
t = tarfile.open(path)
t.getnames()
t.extractall(path='/tmp/some/new/path')
t.close()

# zip
import zipfile
z = zipfile.ZipFile(path)
z.namelist()
z.extractall(path='/tmp/some/new/path')
z.close()

# pickle
import pickle
f = open(path, 'rb')
u = pickle._Unpickler(f)
u.load()
f.close()

# json
import json
json.load(open(path))

# csv
import csv
f = open(path)
reader = csv.reader(f)
for line in reader:
    print(line)
f.close()

# xml
import xml.et
