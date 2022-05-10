from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# 压缩
from lzma import LZMACompressor
compressor = LZMACompressor()
compressor.compress(b'hello world')
compressor.flush()

# 压缩数据
import lzma
lzma.compress(b'hello world')

# 解压缩数据
