import bz2
# Test BZ2Decompressor.eof()
decompressor = bz2.BZ2Decompressor()
eof = decompressor.eof
assert eof, "BZ2Decompressor.eof not 1"
data = decompressor.decompress(b"hello")
eof = decompressor.eof
assert eof, "BZ2Decompressor.eof not 1"
data = decompressor.decompress(b"world")
eof = decompressor.eof
assert eof, "BZ2Decompressor.eof not 1"
# Test BZ2Decompressor.unused_data
compressed = bz2.compress(b"hello")
compressed += bz2.compress(b"world")
compressed += bz2.compress(b"hello")
compressed += bz2.compress(b"world")
compressed += bz2.compress(b"hello")
compressed += bz2.compress(b"world")
decompressor = bz2.BZ2Decompressor()
data = decompressor.dec
