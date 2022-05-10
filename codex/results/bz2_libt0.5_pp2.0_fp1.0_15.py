import bz2
bz2.decompress(bz2.compress(b'hello world!'))

import zlib
zlib.decompress(zlib.compress(b'hello world!'))

import hashlib
md5 = hashlib.md5()
md5.update(b'hello world!')
md5.hexdigest()

sha1 = hashlib.sha1()
sha1.update(b'hello world!')
sha1.hexdigest()

sha256 = hashlib.sha256()
sha256.update(b'hello world!')
sha256.hexdigest()

sha512 = hashlib.sha512()
sha512.update(b'hello world!')
sha512.hexdigest()

import hmac
hmac.new(b'123456', b'hello world!').hexdigest()

import itertools
natuals = itertools.count(1)
for n in natuals:
    print(n)
    if n >= 10:
        break

cs = itertools.cycle('ABC')
for c
