import lzma
# Test LZMADecompressor

# Test decompressor
d = lzma.LZMADecompressor()

# Test decompress()
assert d.decompress(b"") == b""
assert d.decompress(b"\x00") == b"\x00"
assert d.decompress(b"\x00\x00") == b"\x00\x00"
assert d.decompress(b"\x00\x00\x00") == b"\x00\x00\x00"
assert d.decompress(b"\x00\x00\x00\x00") == b"\x00\x00\x00\x00"
assert d.decompress(b"\x00\x00\x00\x00\x00") == b"\x00\x00\x00\x00\x00"
assert d.decompress(b"\x00\x00\x00\x00\x00\x00") == b"\x00\x00\x00\x00\x00\x
