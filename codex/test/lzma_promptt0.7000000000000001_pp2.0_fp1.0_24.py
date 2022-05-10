import lzma
# Test LZMADecompressor.decompress()

magic = b"\xfd7zXZ\x00" + b"\x00" * 6 + b"\xff" * 2

# Test basic operation
d = lzma.LZMADecompressor()
