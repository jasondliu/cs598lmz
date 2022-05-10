from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_data)

# b"Hello, world."

# The LZMA file format is a container format, and the LZMA algorithm is just
# one of the supported compression methods. The LZMA file format also supports
# LZMA2, which is an improved version of the LZMA algorithm.
#
# The LZMA module does not support the LZMA2 compression method.
#
# For details about the LZMA file format, see:
# https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Markov_chain_algorithm
#
# The LZMADecompressor class supports the context manager protocol.

with LZMADecompressor() as decompressor:
    decompressor.decompress(lzma_data)

# b"Hello, world."

# The LZMADecompressor class supports the stream-based decompression
# protocol.

decompressor = LZMADecompressor()
decompressor.decompress(
