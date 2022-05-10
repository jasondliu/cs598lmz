from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'hello world'))

# bz2的压缩和解压可以一起进行，就像一个滑动窗口一样
from bz2 import BZ2Compressor, BZ2Decompressor

compressor = BZ2Compressor()
decompressor = BZ2Decompressor()

compressed_data = compressor.compress(b'hello world')
compressed_data += compressor.flush()

decompressed_data = decompressor.decompress(compressed_data)

print(decompressed_data)

# 压缩和解压缩的过程可以一起进行
compressor = BZ2Compressor()
decompressor = BZ2Decompressor()

compressed_data = compressor.compress(b'hello world')
compressed_data += compressor.
