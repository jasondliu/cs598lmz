import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import lzma
lzma.decompress(lzma.compress(b'hello world'))

import gzip
gzip.decompress(gzip.compress(b'hello world'))

import zipfile
with zipfile.ZipFile('test.zip', 'w', zipfile.ZIP_DEFLATED) as f:
    f.write('test.txt')

with zipfile.ZipFile('test.zip', 'r') as f:
    print(f.namelist())
    print(f.getinfo('test.txt'))
    print(f.read('test.txt'))
    print(f.extractall('.'))

import tarfile
with tarfile.open('test.tar', 'w') as f:
    f.add('test.txt')

with tarfile.open('test.tar', 'r') as f
