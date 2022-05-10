import bz2
# Test BZ2Decompressor's re-used memory.
decomp = bz2.BZ2Decompressor()
s = bz2.compress(b"a" * 1000)
d = decomp.decompress(s)
assert d == b"a" * 1000
