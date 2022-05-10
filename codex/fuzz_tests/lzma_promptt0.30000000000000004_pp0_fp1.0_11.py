import lzma
# Test LZMADecompressor

# Test LZMADecompressor.decompress()

# Test LZMADecompressor.decompress() with empty input
c = lzma.LZMADecompressor()
assert c.decompress(b'') == b''

# Test LZMADecompressor.decompress() with a single byte
c = lzma.LZMADecompressor()
assert c.decompress(b'x') == b'x'

# Test LZMADecompressor.decompress() with a single byte, multiple times
c = lzma.LZMADecompressor()
assert c.decompress(b'x') == b'x'
assert c.decompress(b'y') == b'y'
assert c.decompress(b'z') == b'z'

# Test LZMADecompressor.decompress() with a single byte, multiple times,
# and then some more
c = lzma.LZMADecompressor()
assert c.decomp
