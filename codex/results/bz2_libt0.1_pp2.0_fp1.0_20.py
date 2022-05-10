import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import gzip
with gzip.open('test.gz', 'wt') as f:
    f.write('hello world')

with gzip.open('test.gz', 'rt') as f:
    print(f.read())

import zipfile
with zipfile.ZipFile('test.zip', 'w') as zf:
    zf.write('test.gz')

with zipfile.ZipFile('test.zip', 'r') as zf:
    print(zf.read('test.gz'))

import tarfile
with tarfile.open('test.tar', 'w') as tf:
    tf.add('test.gz')

with tarfile.open('test.tar', 'r') as tf:
    print(tf.extractfile('test.gz').read())

import os
os.chdir('/tmp')
os.getcwd()
