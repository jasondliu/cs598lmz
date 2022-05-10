import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import lzma
lzma.decompress(lzma.compress(b'hello world'))

# 如果你想指定压缩级别，可以传入一个级别参数，级别范围是 1-9。
# 这个参数指定了使用多少内存来缓冲压缩数据，级别越高，压缩越快，但是解压缩速度会慢的多。
# 默认的级别是 9
