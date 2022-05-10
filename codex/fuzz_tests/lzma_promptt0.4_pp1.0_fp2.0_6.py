import lzma
# Test LZMADecompressor

# LZMA is a compression format, which is not a stream format.
# The LZMADecompressor class is a wrapper for the LZMA library,
# which is used to decompress a LZMA stream.

# The LZMA library is not available in the standard library.
# It is included in the Pypy distribution.

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress the data with decompress()
data = b'\x5d\x00\x00\x80\x00\x10\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
