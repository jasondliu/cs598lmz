from lzma import LZMADecompressor
LZMADecompressor().decompress(inbytes)

# 使用通用的接口压缩和解压
# 对于压缩数据，可以使用 zlib.compress() 和 zlib.decompress() 函数。 
# 它们的参数和 lzma 模块一样
import zlib
compressed = zlib.compress(b'This is some data.')
decompressed = zlib.decompress(compressed)

# 对于文件，可以使用 zlib.compress() 和 zlib.decompress() 函数。
# 它们的参数和 lzma 模块一样
import zlib
with open('lorem.txt', 'rb') as input:
    with open('lorem.z', 'wb') as
