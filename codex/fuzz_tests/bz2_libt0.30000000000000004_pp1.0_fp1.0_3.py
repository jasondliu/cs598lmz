import bz2
bz2.BZ2File(path)

# gzip
import gzip
gzip.open(path)

# lzma
import lzma
lzma.open(path)

# zipfile
import zipfile
zipfile.ZipFile(path)

# tarfile
import tarfile
tarfile.open(path)

# pickle
import pickle
pickle.load(path)

# shelve
import shelve
shelve.open(path)

# json
import json
json.load(path)

# csv
import csv
csv.reader(path)

# xml
import xml.etree.ElementTree as et
et.parse(path)

# hdf5
import h5py
h5py.File(path)

# sqlite
import sqlite3
conn = sqlite3.connect(path)

# pandas
import pandas as pd
pd.read_csv(path)

# matplotlib
import matplotlib.pyplot as plt
plt.imread(path)
