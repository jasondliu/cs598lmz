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
zipfile.ZipFile(filename)

# tarfile
import tarfile
tarfile.open(filename)

# pickle
import pickle
pickle.load(open(filename, 'rb'))

# json
import json
json.load(open(filename))

# yaml
import yaml
yaml.load(open(filename))

# csv
import csv
csv.reader(open(filename))

# sqlite3
import sqlite3
conn = sqlite3.connect(filename)
curs = conn.cursor()

# hdf5
import h5py
h5py.File(filename)

# netCDF4
import netCDF4
netCDF4.Dataset(filename)

# xarray
import xarray
xarray.open_dataset(
