import lzma
# Test LZMADecompressor

# Test basic operation
d = lzma.LZMADecompressor()
assert d.decompress(b"") == b""
