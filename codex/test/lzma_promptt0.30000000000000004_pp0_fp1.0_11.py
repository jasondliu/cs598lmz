import lzma
# Test LZMADecompressor

# Test LZMADecompressor.decompress()

# Test LZMADecompressor.decompress() with empty input
c = lzma.LZMADecompressor()
assert c.decompress(b'') == b''

# Test LZMADecompressor.decompress() with a single byte
c = lzma.LZMADecompressor()
