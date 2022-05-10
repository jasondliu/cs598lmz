from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

import bz2
bz2.decompress(compressed)

import zlib
zlib.decompress(compressed)

# 如果你想在不同的压缩方法之间转换数据，你可以使用通用的压缩库zlib
import zlib, bz2, lzma
compressed = zlib.compress(data)
compressed = bz2.compress(data)
compressed = lzma.compress(data)

# 在zlib模块中也有一个常见的压缩方法，叫做deflate。它可以使用zlib模块来进行解压缩，也可以使用gzip或者zipfile
