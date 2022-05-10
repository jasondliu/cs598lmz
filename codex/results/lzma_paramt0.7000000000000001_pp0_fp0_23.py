from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

# bzip2
import bz2
compressed = bz2.compress(original)
bz2.decompress(compressed)

# gzip
import gzip
with gzip.open('somefile.gz', 'wt') as f:
    f.write(original)

with gzip.open('somefile.gz', 'rt') as f:
    print(f.read())

# zlib
import zlib
compressed = zlib.compress(original)
original = zlib.decompress(compressed)

s = b'witch which has which witches wrist watch'
print(len(s))

import zlib
t = zlib.compress(s)
print(len(t))

import bz2
print(len(bz2.compress(s)))

print(zlib.crc32(s))

# 使用标准库中的模块
import timeit
print(timeit.timeit(
    'char in
