from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# b'Hello World!Hello World!Hello World!Hello World!'
# b'Hello World!' * 4

# 使用 LZMA 算法压缩数据
from lzma import LZMACompressor
compressor = LZMACompressor()
compressor.compress(b'Hello World!')
compressor.compress(b'Hello World!')
compressor.compress(b'Hello World!')
compressor.flush()

# b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xcaIU\x01\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xcaIU\x01\x00\x00\x04\xe6\xd6\xb4F\
