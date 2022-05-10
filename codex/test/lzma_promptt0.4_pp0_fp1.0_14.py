import lzma
# Test LZMADecompressor's max_length parameter.
# The data is a big string of 'x' characters, compressed with
# lzma.LZMACompressor(format=lzma.FORMAT_ALONE).
# The decompressor should raise an exception if the max_length
# parameter is too small.
