import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename)

# lzma
import lzma
lzma.LZMAFile(filename)

# tarfile
import tarfile
tarfile.open(filename)

# zipfile
import zipfile
zipfile.ZipFile(filename)

# xml.etree.ElementTree
import xml.etree.ElementTree as ET
ET.parse(filename)

# json
import json
json.load(filename)

# csv
import csv
csv.reader(filename)

# sqlite3
import sqlite3
conn = sqlite3.connect(filename)

# hdf5
import h5py
h5py.File(filename)

# netCDF4
import netCDF4
netCDF4.Dataset(filename)

# pandas
import pandas
pandas.read_csv(filename)

# xarray
import xarray
xarray.open_dataset(filename)

# geopandas
