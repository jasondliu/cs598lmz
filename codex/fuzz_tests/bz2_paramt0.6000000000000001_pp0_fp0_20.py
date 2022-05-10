from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'hello world!'))

import lzma
lzma.decompress(lzma.compress(b'hello world!'))

# 如果压缩数据量比较大，就应该使用基于文件的压缩方式，比如gzip和bz2模块提供的类
import gzip
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

# lzma模块的主要类没有提供任何文件对象接口，但是可以使用LZMAFile类实现
import lzma
with lzma.open('somefile.
