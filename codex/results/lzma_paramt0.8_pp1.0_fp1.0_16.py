from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_data)

# 7.3.4 使用zlib压缩数据

source_data = b'witch which has which witches wrist watch'
len(source_data)

import zlib
compressed = zlib.compress(source_data)
len(compressed)

# 如果想获取更好的压缩率,可以使用1至9的一个数字作为压缩级别
for i in range(10):
    print(i, len(zlib.compress(source_data, i)))

compressed
decompressed = zlib.decompress(compressed)
decompressed

# 7.3.5 使用bz2压缩数据

import bz2
compressed = bz2.compress(source_data)
decompressed = bz2.decompress
