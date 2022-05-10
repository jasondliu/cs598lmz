import bz2
bz2.decompress(bz2.compress(b'hello world'))

import zlib
zlib.decompress(zlib.compress(b'hello world'))

import lzma
lzma.decompress(lzma.compress(b'hello world'))

# 在压缩数据的时候，必须根据目标使用的压缩算法，选择合适的压缩模式。
# 对于文本数据，通常最好的模式就是文本模式，因为它会在压缩的同时保留行尾的换行符。
# 对于非文本数据
