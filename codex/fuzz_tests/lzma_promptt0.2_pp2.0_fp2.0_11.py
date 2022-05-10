import lzma
# Test LZMADecompressor

# Test decompressor
d = lzma.LZMADecompressor()

# Test decompress()
data = d.decompress(b'XZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00')
assert data == b'foo'

# Test flush()
data = d.flush()
assert data == b''

# Test multiple calls to decompress()
d = lzma.LZMADecompressor()
data = d.decompress(b'XZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00')
assert data == b'foo'
data = d.decompress(b'bar')
assert data == b'bar'
data = d.flush()
assert data == b''

# Test multiple calls to decompress() with empty string
d = lzma.LZMAD
