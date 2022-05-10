import bz2
bz2.decompress(bz2.compress(b'hello world!'))

import gzip
with gzip.open('/tmp/file.gz', 'wt') as f:
    f.write('hello world!')

with gzip.open('/tmp/file.gz', 'rt') as f:
    text = f.read()

import zlib
s = b'hello world!'
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)
zlib.crc32(s)

import hashlib
md5 = hashlib.md5()
md5.update(s)
md5.digest()
md5.hexdigest()

sha1 = hashlib.sha1()
sha1.update(s)
sha1.hexdigest()

import hmac
message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
h.hexdigest()

import random
random.
