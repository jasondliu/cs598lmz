import lzma
# Test LZMADecompressor

# Test basic functionality
decomp = lzma.LZMADecompressor()

d = decomp.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x00\x00\x04\x00\x00\x00\x00')
assert d == b'12345abcde'

# Test multiple decompress() calls
decomp = lzma.LZMADecompressor()

d = decomp.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x00\x00\x04\x00\x00\x00\x00')
assert d == b'12345'

d
