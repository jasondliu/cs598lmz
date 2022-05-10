import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import lzma
lzma.decompress(lzma.compress(b'hello world'))

import gzip
with gzip.open('/tmp/test.gz', 'wt') as f:
    f.write('hello world')

with gzip.open('/tmp/test.gz', 'rt') as f:
    print(f.read())

import zipfile
with zipfile.ZipFile('/tmp/test.zip', 'w') as zf:
    zf.write('/tmp/test.gz')

with zipfile.ZipFile('/tmp/test.zip', 'r') as zf:
    print(zf.read('test.gz'))

import tarfile
with tarfile.open('/tmp/test.tar', 'w') as tf:
    tf.add('/tmp/test.gz')

with tarfile
