from lzma import LZMADecompressor
LZMADecompressor().decompress(b'...')

# 使用LZMACompressor来压缩数据
from lzma import LZMACompressor
compressor = LZMACompressor()
data = b'...'
compressor.compress(data)
compressor.flush()

# 压缩和解压文件
import lzma
