from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)
decompressed
# The bz2 module provides a comprehensive interface for the bz2 compression library
# Starting with Python 3.3, the bz2 module provides access to the BZIP2 compression library.
import bz2
compressor = bz2.BZ2Compressor()
compressed = compressor.compompress(data)
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed)
# The zlib module provides a lower-level interface to many of the functions in the zlib library
# The zlib module provides a lower-level interface to many of the functions in the zlib compression library from the GNU project
import zlib
compressor = zlib.compressobj(1)
compressed = compressor.compress(data)
compressed += compressor.flush()
decompressor = zlib.decompressobj()
decompressed = decompressor.decompress(compressed)
decompressed += decompressor.flush()
decompressed
# Memoryview and Bytearray provide types that can be used
