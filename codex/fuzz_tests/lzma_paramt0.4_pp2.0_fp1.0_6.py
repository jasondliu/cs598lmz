from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 如果你想更多的控制压缩和解压缩的过程，可以使用 LZMACompressor 和 LZMADecompressor 类。比如：

import lzma
compressor = lzma.LZMACompressor()
compressor.compress(b'Binary data')
compressor.compress(b'More data')
compressor.flush()

decompressor = lzma.LZMADecompressor()
decompressor.decompress(b'...')
decompressor.decompress(b'...')

# 这个类的使用方式和 zlib.compressobj() 类似。
# 另外一个很有意思的特性是 compress() 和 decompress() 方法
