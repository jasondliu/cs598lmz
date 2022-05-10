import bz2
bz2.BZ2File(filename)

#gzip
import gzip
gzip.open(filename, mode='rt')

#lzma
import lzma
lzma.open(filename)

#zip
import zipfile
zipfile.ZipFile(filename)

#tar
import tarfile
tarfile.open(filename)

#csv
import csv
csv.reader(f)
csv.DictReader(f)

#json
import json
json.load(f)

#pickle
import pickle
pickle.load(f)

#struct
import struct
struct.unpack(fmt, f.read(struct.calcsize(fmt)))

#array
import array
array.array('i', f.read())

#collections
import collections
collections.Counter(word.lower() for line in f for word in line.split())

#mmap
import mmap
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
print(m.readline
