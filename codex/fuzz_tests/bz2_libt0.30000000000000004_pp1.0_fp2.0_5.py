import bz2
bz2.BZ2File(filepath, 'rb')

import gzip
gzip.open(filepath, 'rb')

import lzma
lzma.LZMAFile(filepath)

import zipfile
zf = zipfile.ZipFile(filepath)
zf.namelist()

# Reading from a compressed file
with gzip.open('file.txt.gz', 'rt') as f:
    text = f.read()

# Writing to a compressed file
with gzip.open('file.txt.gz', 'wt') as f:
    f.write(text)

# Reading from a compressed file
with gzip.open('file.txt.gz', 'rt') as f:
    text = f.read()

# Writing to a compressed file
with gzip.open('file.txt.gz', 'wt') as f:
    f.write(text)

# Reading from a compressed file
with bz2.open('file.txt.bz2', 'rt') as f:
    text = f.read()

# Writing
