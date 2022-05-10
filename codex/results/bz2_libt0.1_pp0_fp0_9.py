import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import gzip
f = gzip.open('/tmp/file.gz', 'rb')
f.read()
f.close()

import gzip
with gzip.open('/tmp/file.gz', 'rb') as f:
    f.read()

import gzip
with gzip.open('/tmp/file.gz', 'wt') as f:
    f.write('hello world')

import gzip
with gzip.open('/tmp/file.gz', 'wt') as f:
    f.write('hello world')

import gzip
with gzip.open('/tmp/file.gz', 'wt') as f:
    f.write('hello world')

import gzip
with gzip.open('/tmp/file.gz', 'wt') as f:
    f.write('hello world')

import gzip
with gzip.open('
