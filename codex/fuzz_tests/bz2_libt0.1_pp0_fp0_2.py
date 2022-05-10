import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import lzma
lzma.decompress(lzma.compress(b'hello world'))

import gzip
gzip.decompress(gzip.compress(b'hello world'))

import zipfile
with zipfile.ZipFile('test.zip', 'w') as f:
    f.write('test.txt')

with zipfile.ZipFile('test.zip', 'r') as f:
    print(f.namelist())
    print(f.getinfo('test.txt'))
    print(f.read('test.txt'))

with zipfile.ZipFile('test.zip', 'r') as f:
    print(f.extractall())

with zipfile.ZipFile('test.zip', 'r') as f:
    print(f.extract('test.txt'))

with zipfile.ZipFile('
