from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 另外，还可以指定最大解压缓冲区大小，即使解压数据超过了这个大小也会暂停，并抛出 BufferFull 异常
d = LZMADecompressor(max_length=100)
d.decompress(data)
d.max_length = 200
d.decompress(data)

# 内置的 zlib 模块用于简单的数据压缩和解压缩。
# 使用 compress() 函数来压缩，使用 decompress() 函数来解压缩：
import zlib
s = b'witch which has which witches
