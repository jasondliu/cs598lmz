from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('test.bz2').read())

import bz2
bz2.decompress(open('test.bz2').read())

# gzip
import gzip
gzip.decompress(open('test.gz').read())

# zlib
import zlib
zlib.decompress(open('test.zlib').read())

# lzma
import lzma
lzma.decompress(open('test.xz').read())

# brotli
import brotli
brotli.decompress(open('test.br').read())

# snappy
import snappy
snappy.decompress(open('test.sz').read())

# lz4
import lz4
lz4.decompress(open('test.lz4').read())

# lzf
import lzf
lzf.decompress(open('test.lzf').read())

# lzjb
import lzjb
lzjb.decompress
