from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

# bzip2
import bz2
compressed_data = bz2.compress(original_data)
bz2.decompress(compressed_data)

# zlib
import zlib
compressed_data = zlib.compress(original_data)
zlib.decompress(compressed_data)

# brotli
import brotli
compressed_data = brotli.compress(original_data)
brotli.decompress(compressed_data)

# lz4
import lz4.block
compressed_data = lz4.block.compress(original_data)
lz4.block.decompress(compressed_data)

# lz4
import lz4.frame
compressed_data = lz4.frame.compress(original_data)
lz4.frame.decompress(compressed_data)

# zstandard
import zstandard
compressed_data = zstandard.ZstdCompressor().compress(original_
