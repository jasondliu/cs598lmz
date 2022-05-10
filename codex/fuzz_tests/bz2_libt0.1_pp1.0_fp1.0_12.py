import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import lzma
lzma.decompress(lzma.compress(b'hello world'))

# 如果你想指定压缩级别，可以传入一个级别参数，级别范围是1-9，级别越高，压缩的越好，但是耗时的也越多。
zlib.compress(b'hello world', 9)

# 压缩文件
import gzip
with gzip.open('somefile.gz', 'wt') as f:
    f.write('hello world')

with gzip.open('somefile.gz',
