from lzma import LZMADecompressor
LZMADecompressor()

# s = lzma.compress(b'Hello, world!', format=lzma.FORMAT_RAW, preset=9)
# print(len(lzma.decompress(s)))

import zlib
zlib.compress(b'Hello, world!', 9) # zlib.decompress()

import bz2
bz2.compress(b'Hello, world!', 9) # bz2.decompress()

# 如果要对二进制数据进行解压缩，可以使用 gzip、bz2、lzma
# 或者 zlib 模块。但是由于 gzip.compress() 和 gzip.decompress()
# 方法只能处理单个独立的文件，所以要想像 tar 格式一
