import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename)

# lzma
import lzma
lzma.open(filename)

# tar
import tarfile
tarfile.open(filename)

# zip
import zipfile
zipfile.ZipFile(filename)

# json
import json
json.load(filename)

# csv
import csv
csv.reader(filename)

# xml
import xml.etree.ElementTree as et
et.parse(filename)

# html
from bs4 import BeautifulSoup
BeautifulSoup(filename)

# sqlite
import sqlite3
conn = sqlite3.connect(filename)

# pickle
import pickle
pickle.load(filename)

# excel
import pandas as pd
pd.read_excel(filename)

# hdf5
import h5py
h5py.File(filename)

# netcdf
import netCDF4
netCDF4.Dataset(filename)

