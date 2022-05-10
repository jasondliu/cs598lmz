from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 数据压缩
import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

# 利用zlib来压缩数据
import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

# 利用bz2来压缩数据
import bz2
s = b'witch which has which witches wrist watch'
len(s)

t = bz2.compress(s)
len(t)

bz2.decompress(t)

# 利用lzma来压
