from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

#bz2
from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

#zlib
import zlib
zlib.decompress(data)

# 压缩算法比较
# 压缩速度：lzma > bz2 > zlib
# 压缩比：zlib > bz2 > lzma
# 综合比较：zlib > bz2 > lzma

# 压缩和解压缩文件
# 压缩
import gzip
import bz2
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)

# 解压缩
