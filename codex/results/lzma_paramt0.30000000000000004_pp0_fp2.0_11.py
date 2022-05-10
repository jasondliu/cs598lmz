from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

# b'The quick brown fox jumps over the lazy dog.'

# The LZMA library supports a number of different compression filters,
# including LZMA1 and LZMA2. The LZMADecompressor class can be used to decompress
# data compressed with any of the supported compression filters.
#
# The LZMADecompressor class supports incremental decompression.
#
# The LZMADecompressor class supports the context management protocol.
# Entering a context will call the open() method on the compressor object,
# and exiting the context will call the flush() and close() methods.
#
# The LZMADecompressor class supports the iterator protocol.
# Each call to the next() method will return a chunk of decompressed data.
#
# The LZMADecompressor class supports the file interface.
# Reading data from a file-like object will return decompressed data.
#
# The LZMADecompressor class supports the flush() method.
#
# The LZMADecompressor class supports the copy() method
