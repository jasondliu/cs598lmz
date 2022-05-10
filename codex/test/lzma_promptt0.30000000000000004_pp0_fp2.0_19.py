import lzma
# Test LZMADecompressor

# Test LZMADecompressor.decompress()
decompressor = lzma.LZMADecompressor()

# Test LZMADecompressor.decompress() with a small input
assert decompressor.decompress(b"") == b""
