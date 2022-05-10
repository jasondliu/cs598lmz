import bz2
bz2.BZ2File(filename)

import gzip
gzip.open(filename)

import lzma
lzma.LZMAFile(filename)

# Writing Compressed Data to Files

import bz2
with bz2.BZ2File('file.bz2', 'w') as f:
    f.write(b'Hello World')

import gzip
with gzip.open('file.gz', 'wt') as f:
    f.write('Hello World')

import lzma
with lzma.open('file.xz', 'wt') as f:
    f.write('Hello World')

# Reading and Writing Compressed Data in Memory

import bz2
compressed = bz2.compress(b'Hello World')
bz2.decompress(compressed)

import gzip
compressed = gzip.compress(b'Hello World')
gzip.decompress(compressed)

import lzma
compressed = lzma.compress(b'Hello World')
lzma
