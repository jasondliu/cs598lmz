import lzma
# Test LZMADecompressor.flush()

# Test LZMADecompressor.flush() with no input data

d = lzma.LZMADecompressor()
assert d.flush() == b""

# Test LZMADecompressor.flush() with an EOF marker

data = lzma.compress(b"foo", format=lzma.FORMAT_ALONE) + b"\x00"
d = lzma.LZMADecompressor()
assert d.decompress(data) == b"foo"
assert d.flush() == b""

# Test LZMADecompressor.flush() with a non-EOF marker

data = lzma.compress(b"foo", format=lzma.FORMAT_ALONE) + b"\xff"
d = lzma.LZMADecompressor()
assert d.decompress(data) == b"foo"
assert d.flush() == b""

# Test LZMADecompressor.flush() with a truncated EOF marker

data =
