import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename, mode='rb')

# lzma
import lzma
lzma.open(filename)

# zip
import zipfile
zipfile.ZipFile(filename)

# tar
import tarfile
tarfile.open(name=filename, mode='r:gz')

# csv
import csv
csv.reader(open(filename))

# json
import json
json.load(open(filename))

# xml
import xml.etree.ElementTree as etree
etree.parse(filename)

# pickle
import pickle
pickle.load(open(filename, 'rb'))

# shelve
import shelve
shelve.open(filename)

# sqlite3
import sqlite3
conn = sqlite3.connect(filename)

# hdf5
import h5py
h5py.File(filename)

# matlab
import scipy.io
scipy.io.loadmat(filename)
