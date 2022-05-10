import lzma
# Test LZMADecompressor.
d = lzma.LZMADecompressor()
d.decompress(b"")
d.decompress(b"X" * 10)
d.decompress(b"X" * 1000000)

# Test decompress().
lzma.decompress(b"")
lzma.decompress(b"X" * 10)
lzma.decompress(b"X" * 1000000)

# Test LZMACompressor.
c = lzma.LZMACompressor()
c.compress(b"")
c.compress(b"X" * 10)
c.compress(b"X" * 1000000)
c.flush()

# Test compress().
lzma.compress(b"")
lzma.compress(b"X" * 10)
lzma.compress(b"X" * 1000000)

# Test LZMADecompressor.copy().
d = lzma.LZMADecompressor()
d.decompress(b
