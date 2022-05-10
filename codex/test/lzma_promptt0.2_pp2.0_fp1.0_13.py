import lzma
# Test LZMADecompressor

# Test basic functionality
comp = lzma.LZMADecompressor()
assert comp.decompress(b"") == b""
