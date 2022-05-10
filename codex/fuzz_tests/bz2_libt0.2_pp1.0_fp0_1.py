import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import lzma
lzma.decompress(lzma.compress(b'hello world'))

# 如果要压缩的数据量很大，通常我们先压缩到一个临时文件中，再从临时文件中读取压缩后的数据，这样可以避免大量占用内存。
import gzip
with gzip.open('/tmp/test.gz', 'wt') as f:
    f.write('hello world')

with gzip.open('/tmp/test.gz', 'rt') as f:
    print(f.read())

#
