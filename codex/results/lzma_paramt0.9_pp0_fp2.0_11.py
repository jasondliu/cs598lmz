from lzma import LZMADecompressor
LZMADecompressor

uncompressed_data = LZMADecompressor().decompress(compresseed_data)
print(uncompressed_data)

import bz2
compressed_data = bz2.compress(orig_data)


decompressor = bz2.BZ2Decompressor()
uncompressed_data = decompressor.decompress(compressed_data)
print(uncompressed_data)

#使用zlib来对所有类型的数据进行压缩
import zlib
compressed_data = zlib.compress(orig_data)
uncompressed_data = zlib.decompress(compressed_data)
print(uncompressed_data)

#选择合适的算法和级别 所有压缩工具都提供了调整压缩级别的选
