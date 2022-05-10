import bz2
bz2.decompress(bz2.compress(b'hello world'))

import gzip
gzip.compress(b'hello world')

import zlib
zlib.compress(b'hello world')

import zipfile
with zipfile.ZipFile('test.zip', 'w') as zf:
    zf.write('test.txt')

with zipfile.ZipFile('test.zip', 'r') as zf:
    print(zf.namelist())
    print(zf.getinfo('test.txt'))
    print(zf.read('test.txt'))

with zipfile.ZipFile('test.zip', 'r') as zf:
    zf.extractall()

with zipfile.ZipFile('test.zip', 'r') as zf:
    zf.extract('test.txt', 'tmp')

with zipfile.ZipFile('test.zip', 'a') as zf:
    zf.write('test.txt')

import tarfile
with tarfile.open('test.
