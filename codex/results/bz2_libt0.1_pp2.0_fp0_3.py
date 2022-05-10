import bz2
bz2.decompress(bz2.compress(b'hello world'))

import gzip
with gzip.open('/tmp/file.gz', 'wt') as f:
    f.write('hello world')

with gzip.open('/tmp/file.gz', 'rt') as f:
    text = f.read()

import zlib
s = b'hello world'
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)
zlib.crc32(s)

import hashlib
hashlib.md5(b'hello world').hexdigest()
hashlib.sha1(b'hello world').hexdigest()
hashlib.sha256(b'hello world').hexdigest()

import hmac
h = hmac.new(b'secret-shared-key-goes-here', b'hello world', hashlib.sha1)
h.hexdigest()

import random
random.seed(1)
random.random()
random.randint(
