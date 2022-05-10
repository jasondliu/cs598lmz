import lzma
# Test LZMADecompressor

# Test basic functionality
comp = lzma.LZMADecompressor()
assert comp.decompress(b"") == b""
assert comp.decompress(b"\x00") == b"\x00"
assert comp.decompress(b"\x00\x00") == b"\x00\x00"
assert comp.decompress(b"\x00\x00\x00") == b"\x00\x00\x00"
assert comp.decompress(b"\x00\x00\x00\x00") == b"\x00\x00\x00\x00"
assert comp.decompress(b"\x00\x00\x00\x00\x00") == b"\x00\x00\x00\x00\x00"
assert comp.decompress(b"\x00\x00\x00\x00\x00\x00") == b"\x00\x00\x00\x00\x00\x00"
assert comp.dec
