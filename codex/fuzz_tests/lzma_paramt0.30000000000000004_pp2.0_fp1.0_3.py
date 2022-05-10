from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# b'hello world\n'

# 如果数据是压缩的，但是不知道压缩的算法，可以使用第三方库 backports.lzma 来检测数据的压缩算法。

from backports import lzma
lzma.detect_compression(data)

# 'lzma'

# 如果数据是压缩的，但是不知道压缩的算法，可以使用第三方库 backports.lzma 来检测数据的压缩算法。

from backports import lzma
lzma.detect_compression(data)

#
