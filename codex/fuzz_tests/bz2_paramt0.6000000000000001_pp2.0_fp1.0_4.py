from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(data))

# 使用lzma库
import lzma
lzma.decompress(lzma.compress(data))

# 如果你想自己实现压缩的功能，可以使用zlib库
import zlib
zlib.compress(data)
zlib.decompress(zlib.compress(data))

# 如果你想控制压缩级别，可以使用compressobj() 函数来代替压缩函数
compressor = zlib.compressobj(1)
compressor.compress(data)
compressor.flush()
# 'x\234K\313\311OR\312\315\311N\311\312\316K\311\313OR\311\312\315I\313\
