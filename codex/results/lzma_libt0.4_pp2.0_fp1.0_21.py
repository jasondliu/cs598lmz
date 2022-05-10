import lzma
lzma.decompress(lzma.compress(b'Hello World'))

import bz2
bz2.decompress(bz2.compress(b'Hello World'))

import zlib
zlib.decompress(zlib.compress(b'Hello World'))

import gzip
gzip.decompress(gzip.compress(b'Hello World'))

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
    print(f.getmember('test.py'
