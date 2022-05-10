import lzma
lzma_compressor = lzma.LZMACompressor()
# Append bytes to the compressor object
lzma_compressor.compress(b"foo")
# Returns the compressed data so far, as a bytes object.
lzma_compressor.flush()
# Returns the bytes left after decompressing
