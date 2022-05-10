import bz2
bz2.BZ2File(filename)

import gzip
gzip.open(filename, mode='rt')

import lzma
lzma.open(filename)

# Reading from archives
with bz2.open(filename, mode='rt') as f:
    data = f.read()

with gzip.open(filename, mode='rt') as f:
    data = f.read()

with lzma.open(filename, mode='rt') as f:
    data = f.read()

# Writing to archives
with bz2.open(filename, mode='wt') as f:
    f.write(data)

with gzip.open(filename, mode='wt') as f:
    f.write(data)

with lzma.open(filename, mode='wt') as f:
    f.write(data)

# Reading and writing raw bytes
with bz2.open(filename, mode='rb') as f:
    data = f.read()

with gzip.open(filename, mode='rb') as f:

