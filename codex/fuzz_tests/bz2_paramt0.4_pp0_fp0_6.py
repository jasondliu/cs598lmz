from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

import zlib
zlib.decompress(data)

import gzip
gzip.decompress(data)

import lzma
lzma.decompress(data)

# 压缩数据
import bz2
bz2.compress(data)

import zlib
zlib.compress(data)

import gzip
gzip.compress(data)

import lzma
lzma.compress(data)

# 压缩和解压缩文件
import gzip
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

# 压缩和解压缩数据
import gzip
s = b'Hello World!'
t = gzip.compress(s)
gzip
