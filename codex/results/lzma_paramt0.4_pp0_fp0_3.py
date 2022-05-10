from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

# bz2
import bz2
compressed_data = bz2.compress(original_data)
original_data == bz2.decompress(compressed_data)

# zlib
import zlib
compressed_data = zlib.compress(original_data)
original_data == zlib.decompress(compressed_data)

# zlib
import zlib
compressed_data = zlib.compress(original_data)
original_data == zlib.decompress(compressed_data)

# brotli
import brotli
compressed_data = brotli.compress(original_data)
original_data == brotli.decompress(compressed_data)

# blosc
import blosc
compressed_data = blosc.compress(original_data)
original_data == blosc.decompress(compressed_data)

# snappy
import snappy
compressed_data = snappy.compress(original_data)
original_
