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
    zf.write('test.py')

with zipfile.ZipFile('test.zip', 'r') as zf:
    print(zf.namelist())
    print(zf.getinfo('test.py'))
    print(zf.read('test.py'))

with zipfile.ZipFile('test.zip', 'a') as zf:
    zf.write('test.py', 'test2.py')

with zipfile.ZipFile('test.zip', 'r') as zf:
    print(zf.nam
