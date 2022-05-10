import bz2
bz2.BZ2File('data/file.bz2').read() # bz2 compressed file

import gzip
gzip.open('data/file.gz').read() # gzip compressed file

import zipfile
zipfile.ZipFile('data/file.zip').read('file.txt') # zipped file

import tarfile
tarfile.open('data/file.tar.gz').extractall() # tarball

import h5py
h5py.File('data/file.hdf5').get('data') # HDF5 file

import csv
with open('data/file.csv') as f:
    reader = csv.reader(f)
    reader.next() # csv file

import json
with open('data/file.json') as f:
    f.read()

import xml
with open('data/file.xml') as f:
    f.read()
 
import pickle
pickle.load(open('data/file.pkl', 'rb')) # pickled file
```

* 파
