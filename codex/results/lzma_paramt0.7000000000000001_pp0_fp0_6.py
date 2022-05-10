from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_data)

# 如果要处理的压缩数据分块编码的，可以使用decompress()方法的iterdecompress()方法

decompressor = LZMADecompressor()
for piece in pieces:
    # 每次调用返回一部分解压后的数据
    if piece:
        data = decompressor.decompress(piece)
    else:
        data = decompressor.flush()


# 12.4 使用zlib压缩数据

import zlib
s = b'witch which has which witches wrist watch'
len(s)

# 可以使用zlib.compress()函数来压缩数据
t = zlib.compress(s)
len(t)
