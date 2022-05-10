import bz2
bz2.BZ2File(filename)

import gzip
gzip.open(filename, mode='rt')

import lzma
lzma.open(filename)

# Writing compressed data to a file
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

# Reading compressed data from a file
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

# Reading and Writing Binary Data
data = b'Hello World'
with open('somefile.bin', 'wb') as f:
    f.write(data)

with open('somefile.bin', 'rb') as f:
    data = f.read()

# Writing Text Data
with open('hello.txt', 'w') as f:
    f.write('hello, world!')

# Reading Text Data
with open('hello.txt', 'r') as f:
    s = f.read()

# Reading and Writing Binary Data
with open('somefile.bin', 'wb') as f:
