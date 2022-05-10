import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import lzma
lzma.decompress(lzma.compress(b'hello world'))

# 如果你想控制压缩级别，可以传入一个级别参数，级别范围是 1-9。
# 这个参数指定了使用多少CPU时间来压缩，级别越高，压缩越慢，但是压缩后的数据越小。

# 压缩文件
# 压缩文件的一
