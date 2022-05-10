import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

import zlib
zlib.decompress(zlib.compress(b'Hello World!'))

import gzip
with gzip.open('test.gz', 'rt') as f:
    text = f.read()

import zipfile
with zipfile.ZipFile('test.zip') as zf:
    print(zf.namelist())
    print(zf.getinfo('test.txt'))
    print(zf.read('test.txt'))

with zipfile.ZipFile('test.zip', 'w') as zf:
    zf.write('test.txt')
    zf.write('test.txt.bz2')

from io import BytesIO
import tarfile
b = BytesIO()
with tarfile.open(mode='w', fileobj=b) as tf:
    tf.add('test.txt')
    tf.add('test.txt.bz2')

b.getvalue()

with tarfile.open
