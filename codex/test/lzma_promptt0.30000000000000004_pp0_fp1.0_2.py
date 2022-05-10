import lzma
# Test LZMADecompressor

# Test basic functionality

d = lzma.LZMADecompressor()
assert d.unused_data == b""
assert d.eof is False

# Test decompression

data = lzma.compress(b"test")
assert d.decompress(data) == b"test"
assert d.unused_data == b""
assert d.eof is True

# Test that decompression fails after eof

