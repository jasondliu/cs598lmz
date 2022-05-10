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
    print(zf.namelist())
    print(zf.getinfo('test.txt'))
    print(zf.read('test.txt'))

zf.extractall('test')

with zipfile.ZipFile('test.zip', 'a') as zf:
    zf.write('test.txt')

with zipfile.ZipFile('test.zip', 'r') as zf:
    print
