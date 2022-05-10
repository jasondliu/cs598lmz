import bz2
bz2.BZ2File(DATA_PATH+'data.json.bz2', 'rb')

import gzip
gzip.open(DATA_PATH+'data.json.gz', 'rb')

import lzma
lzma.LZMAFile(DATA_PATH+'data.json.xz', 'rb')

import sqlite3
conn = sqlite3.connect(DATA_PATH+'data.sqlite')

import hdf5
import h5py
f = h5py.File(DATA_PATH+'data.hdf5', 'r')

import feather
feather.read_dataframe(DATA_PATH+'data.feather')

import parquet
pq.ParquetFile(DATA_PATH+'data.parquet').read()

import msgpack
import msgpack_numpy
msgpack.unpackb(open(DATA_PATH+'data.msgpack', 'rb').read(), object_hook=msgpack_numpy.decode)

import csv
csv.DictReader(open(DATA_PATH+'data
