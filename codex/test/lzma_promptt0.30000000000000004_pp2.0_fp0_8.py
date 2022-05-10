import lzma
# Test LZMADecompressor.

# Create a decompressor object.
decompressor = lzma.LZMADecompressor()

# Feed one byte at a time to the decompressor.
# This will raise an EOFError when the end of the compressed data
# has been reached.
