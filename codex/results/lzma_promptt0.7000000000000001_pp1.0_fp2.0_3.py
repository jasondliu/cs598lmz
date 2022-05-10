import lzma
# Test LZMADecompressor with a single-byte input stream.
d = lzma.LZMADecompressor()
assert d.decompress(b's') == b's'
# Test LZMADecompressor with a two-byte input stream.
assert d.decompress(b'e') == b'e'
# Test LZMADecompressor with a three-byte input stream.
assert d.decompress(b'k') == b'k'
# Test LZMADecompressor with a four-byte input stream.
assert d.decompress(b'i') == b'i'
# Test LZMADecompressor with a five-byte input stream.
assert d.decompress(b'n') == b'n'
# Test LZMADecompressor with a six-byte input stream.
assert d.decompress(b'g') == b'g'
# Test LZMADecompressor with a seven-byte input stream.
assert d.decompress(b'!') == b'!'
# Test LZMADecomp
