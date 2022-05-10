import lzma
# Test LZMADecompressor.decompress() with a large input
#
# Decompresses the data from the file 'lzma_stream_large.xz'.
#
# The data is a stream of 10,000,000 copies of the same small string,
# 'Hello, world!'.  The data is compressed using the default LZMA
# settings, which is a preset dictionary of 2^23 bytes (8 MiB).
#
# The small string is not compressible with the preset dictionary, and
# it's also too small to be compressed even with a preset dictionary of
# 2^24 bytes (16 MiB).  Thus, the compressed data consists of a large
# number of short uncompressed chunks.

# Read the compressed data from the file
