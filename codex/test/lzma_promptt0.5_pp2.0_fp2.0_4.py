import lzma
# Test LZMADecompressor with a decompression object

# First, create a decompression object
d = lzma.LZMADecompressor()

# Then, feed data to it. The compressed data is fed in chunks
# to avoid overloading the decompressor with too much data.
# This is especially important when decompressing large files.
