import lzma
# Test LZMADecompressor and LZMACompressor
# Note that LZMADecompressor doesn't support the buffered API yet

# Decompressor

d = lzma.LZMADecompressor()

# Basic operation

assert d.decompress(b"") == b""
assert d.decompress(b"x") == b"x"
assert d.decompress(b"xy") == b"xy"
assert d.decompress(b"xyz") == b"xyz"

# Compressed data

cdata = lzma.compress(b"xyz")
assert d.decompress(cdata) == b"xyz"

# Multiple calls

assert d.decompress(cdata[:1]) == b""
assert d.decompress(cdata[1:2]) == b""
assert d.decompress(cdata[2:]) == b"xyz"

# Multiple streams

assert d.decompress(cdata + cdata) == b"xyzxyz"

# Error handling


