import bz2
bz2.decompress(bz2.compress(b'Hello World'))

import zlib
zlib.decompress(zlib.compress(b'Hello World'))

import lzma
lzma.decompress(lzma.compress(b'Hello World'))

import gzip
gzip.decompress(gzip.compress(b'Hello World'))

import zipfile
with zipfile.ZipFile('test.zip', 'w') as zf:
    zf.write('test.txt')

with zipfile.ZipFile('test.zip', 'r') as zf:
    print(zf.namelist())
    print(zf.read('test.txt'))

with zipfile.ZipFile('test.zip', 'a') as zf:
    zf.write('test.txt')

with zipfile.ZipFile('test.zip', 'r') as zf:
    print(zf.namelist())
    print(zf.read('test.txt'))

with zipfile
