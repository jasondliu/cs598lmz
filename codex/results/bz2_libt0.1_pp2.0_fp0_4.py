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
    f.write('test.py')

with zipfile.ZipFile('test.zip', 'r') as f:
    print(f.namelist())
    print(f.getinfo('test.py'))
    print(f.read('test.py'))

import tarfile
with tarfile.open('test.tar', 'w') as f:
    f.add('test.py')

with tarfile.open('test.tar', 'r') as f:
    print(f.getnames())
    print(f.getmember('test.py
