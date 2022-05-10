import lzma
# Test LZMADecompressor.read() with a too large value for max_length.
# The max_length keyword argument of LZMADecompressor.read() should prevent
# the decompressor from consuming more than max_length bytes of input data.
MAX_SIZE = 2**31 - 1
decomp = lzma.LZMADecompressor()
compressed = b'\x00'*(MAX_SIZE + 1)
# Attempting to decompress more than MAX_SIZE bytes must raise an exception
