import bz2
# Test BZ2Decompressor class
dec = bz2.BZ2Decompressor()
dec.decompress(comptxt)

# We can decompress an entire file at once, but decompress() can only do one stream.

# Rename file bzfile.txt.tar.bz2
bzfile = bz2.BZ2File('bzfile.txt.tar.bz2')
bzfile.readlines()


# BZ2File class is a context manager
with bz2.open('bzfile.txt.tar.bz2') as bfile:
    lines = bfile.readlines()
    for line in lines:
        print(line)

# Gzip
# In module gzip, we neet to import gzip, import time
import gzip

# Writing compressed files

import gzip
# There is a default extension ".gz"
fname = 'newfile.txt'
with gzip.open(fname, 'w') as f:
    f.write('Text to write in a compressed file')
with gzip.open(fname, '
