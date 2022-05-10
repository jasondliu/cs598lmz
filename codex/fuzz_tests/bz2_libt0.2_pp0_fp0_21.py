import bz2
bz2.decompress(bz2.compress(b'hello world!'))

import zlib
zlib.decompress(zlib.compress(b'hello world!'))

import lzma
lzma.decompress(lzma.compress(b'hello world!'))

import gzip
gzip.decompress(gzip.compress(b'hello world!'))

import zipfile
with zipfile.ZipFile('test.zip', 'w') as zf:
    zf.write('test.txt')

with zipfile.ZipFile('test.zip', 'r') as zf:
    zf.extractall()

with zipfile.ZipFile('test.zip', 'r') as zf:
    for name in zf.namelist():
        print(name)

with zipfile.ZipFile('test.zip', 'r') as zf:
    for info in zf.infolist():
        print(info.filename)

with zipfile.ZipFile('test.zip', 'r') as z
