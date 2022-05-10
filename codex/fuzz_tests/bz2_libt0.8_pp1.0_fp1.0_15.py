import bz2
bz2.BZ2Decompressor().decompress(bz2file)

# https://blog.csdn.net/v_july_v/article/details/8416356

import _pickle as cPickle
cPickle.loads(bz2file)


# -------------------------------------------------------------------------

import gzip
gzipfile = b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x00\xff\x06\xe5\xe0\x7c\x00\x10\x00\x00\x00\x00\x00\x100\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

gz = gzip.GzipFile(fileobj=gzipfile)
print(gz.read())

import zlib
print(zlib.decompress(gzipfile))
