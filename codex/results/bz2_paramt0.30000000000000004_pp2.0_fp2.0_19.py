from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# 如果你想控制压缩块的大小，可以使用 compress() 和 decompress() 方法
dec = BZ2Decompressor()
dec.decompress(data)
dec.decompress(more_data)

# 压缩数据的编码和解码
data = b'Hello World'
len(data)

import zlib
s = zlib.compress(data)
len(s)

t = zlib.decompress(s)
t

# 如果你想控制压缩级别，可以传递一个级别参数
s = zlib.compress(data, 9)
len(s)

t = zlib.decompress(s)
t

#
