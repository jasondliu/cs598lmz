import lzma
# Test LZMADecompressor

# Test that the decompressor can handle a single-byte input
d = lzma.LZMADecompressor()
assert d.decompress(b"\x00") == b""

# Test that the decompressor can handle a single-byte input with a dictionary
