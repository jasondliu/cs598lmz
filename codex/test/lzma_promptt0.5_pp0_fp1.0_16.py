import lzma
# Test LZMADecompressor.decompress()

# Test with a buffer that is smaller than the input.
decompressor = lzma.LZMADecompressor()
