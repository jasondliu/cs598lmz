from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 压缩
from lzma import LZMACompressor
compressor = LZMACompressor()
compressor.compress(b'Some data')
compressor.flush()

# 压缩和解压缩数据
from lzma import LZMADecompressor, LZMACompressor
compressor = LZMACompressor()
data = b'Some data'
compressed = compressor.compress(data)
compressed += compressor.flush()

decompressor = LZMADecompressor()
decompressor.decompress(compressed)

# 压缩和解压缩文件
from lzma import LZMADecompressor, LZMACompressor
with open('somefile.xz', 'rb') as input, open('somefile.out', 'wb') as output:
    decompressor = LZMADecompressor()
    for block in iter(lambda: input.read
