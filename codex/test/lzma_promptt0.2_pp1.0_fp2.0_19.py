import lzma
# Test LZMADecompressor

# Test basic functionality
d = lzma.LZMADecompressor()
assert d.decompress(b"") == b""
