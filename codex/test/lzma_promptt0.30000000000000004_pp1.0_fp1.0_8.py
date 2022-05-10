import lzma
# Test LZMADecompressor

# Test that the decompressor object can be used to decompress data after
# the end-of-stream marker has been found.

decompressor = lzma.LZMADecompressor()

