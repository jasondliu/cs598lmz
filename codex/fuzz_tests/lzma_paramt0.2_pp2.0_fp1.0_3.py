from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 压缩
from lzma import LZMACompressor
compressor = LZMACompressor()
compressor.compress(b"some data")
compressor.flush()

# 压缩和解压缩
from lzma import LZMADecompressor, LZMACompressor
compressor = LZMACompressor()
decompressor = LZMADecompressor()
compressed = compressor.compress(b"some data")
compressed += compressor.flush()
decompressed = decompressor.decompress(compressed)

# 压缩和解压缩
from lzma import LZMADecompressor, LZMACompressor
compressor = LZMACompressor()
decompressor = LZMADecompressor()
compressed = compressor.compress(b"some data")
compressed += compressor.flush()
decompressed = decompressor.decompress(compressed)

# 压
