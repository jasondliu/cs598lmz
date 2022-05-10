import lzma
# Test LZMADecompressor in LZMACompressor mode.
compressor = lzma.LZMACompressor()

compressed = compressor.compress(b"Example data!")
compressed += compressor.flush()
compressed

decompressor = lzma.LZMADecompressor()

decompressed = decompressor.decompress(compressed)
decompressed

import bz2
# Test BZ2Compressor in BZ2Decompressor mode.
compressor = bz2.BZ2Compressor()

compressed = compressor.compress(b"Example data!")
compressed += compressor.flush()
compressed

decompressor = bz2.BZ2Decompressor()

decompressed = decompressor.decompress(compressed)
decompressed

import zlib
# Test ZlibCompressor in ZlibDecompressor mode.
compressor = zlib.compressobj()

compressed = compressor.compress(b"Example data!")
compressed += compressor.flush()
compressed

