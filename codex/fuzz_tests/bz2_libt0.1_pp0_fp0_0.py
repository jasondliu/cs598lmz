import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import lzma
lzma.decompress(lzma.compress(b'hello world'))

import gzip
gzip.decompress(gzip.compress(b'hello world'))

import zipfile
with zipfile.ZipFile('test.zip', 'w') as zf:
    zf.write('test.txt')

with zipfile.ZipFile('test.zip', 'r') as zf:
    zf.extractall()

import tarfile
with tarfile.open('test.tar', 'w') as tf:
    tf.add('test.txt')

with tarfile.open('test.tar', 'r') as tf:
    tf.extractall()

import os
os.remove('test.txt')
os.remove('test.zip')
os.remove('test.tar')

import shutil

