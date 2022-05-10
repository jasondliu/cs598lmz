import bz2
# Test BZ2Decompressor
c = bz2.BZ2Compressor()
d = c.compress(b'9')
d += c.compress(b'8')
d += c.compress(b'7')
d += c.flush()
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(d)

