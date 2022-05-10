import lzma
# Test LZMADecompressor.

# Test decompression of empty data.
d = lzma.LZMADecompressor()
assert d.decompress(b"") == b""
assert d.unused_data == b""

# Test decompression of a single byte.
d = lzma.LZMADecompressor()
assert d.decompress(b"\x00") == b""
assert d.unused_data == b"\x00"

# Test decompression of a single byte.
d = lzma.LZMADecompressor()
assert d.decompress(b"\x00\x00") == b""
assert d.unused_data == b"\x00\x00"

# Test decompression of a single byte.
d = lzma.LZMADecompressor()
assert d.decompress(b"\x00\x00\x00") == b""
assert d.unused_data == b"\x00\x00\x00"

# Test decompression of a single byte.
d
