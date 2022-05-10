import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import lzma
lzma.decompress(lzma.compress(b'hello world'))

import gzip
f = gzip.open('/tmp/file.gz', 'wt')
f.write('hello world')
f.close()

import gzip
f = gzip.open('/tmp/file.gz', 'rt')
text = f.read()
f.close()

import gzip
with gzip.open('/tmp/file.gz', 'wt') as f:
    f.write('hello world')

import gzip
with gzip.open('/tmp/file.gz', 'rt') as f:
    text = f.read()

import bz2
with bz2.open('/tmp/file.bz2', 'wt') as f:
    f.write('hello world')

import bz2
with
