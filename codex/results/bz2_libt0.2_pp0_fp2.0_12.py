import bz2
bz2.decompress(bz2.compress(b'Hello World'))

import gzip
with gzip.open('test.gz', 'wt') as f:
    f.write('Hello World')

with gzip.open('test.gz', 'rt') as f:
    text = f.read()

import zlib
zlib.compress(b'Hello World')
zlib.decompress(zlib.compress(b'Hello World'))

import zipfile
with zipfile.ZipFile('test.zip', 'w') as f:
    f.write('test.txt')

with zipfile.ZipFile('test.zip', 'r') as f:
    text = f.read('test.txt')

import tarfile
with tarfile.open('test.tar', 'w') as f:
    f.add('test.txt')

with tarfile.open('test.tar', 'r') as f:
    text = f.extractfile('test.txt').read()

import shutil
shutil.copy('test.
