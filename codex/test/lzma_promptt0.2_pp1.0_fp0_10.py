import lzma
# Test LZMADecompressor
# https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte at a time and feed it to the decompressor
