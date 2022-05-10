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

# pathlib
from pathlib import Path
p = Path(filename)
p.read_bytes()
p.read_text()
p.read_bytes()

# mmap
import mmap
with open(filename, 'rb', buffering=0) as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# pickle
import pickle
with open(filename, 'rb') as f:
    pickle.load(f)

# shelve
import shelve
with shelve.open(filename) as db:
    db['key']

# sqlite3
import sqlite3
conn = sqlite3.connect(filename)
