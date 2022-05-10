import lzma
# Test LZMADecompressor

# Test LZMADecompressor.decompress()

# Test LZMADecompressor.decompress() with no data
c = lzma.LZMADecompressor()
c.decompress(b'')

# Test LZMADecompressor.decompress() with partial data
c = lzma.LZMADecompressor()
