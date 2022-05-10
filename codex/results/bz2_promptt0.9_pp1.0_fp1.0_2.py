import bz2
# Test BZ2Decompressor's re-used memory.
decomp = bz2.BZ2Decompressor()
s = bz2.compress(b"a" * 1000)
d = decomp.decompress(s)
assert d == b"a" * 1000
try:
    d = decomp.decompress(b"not bzipped data")
except IOError:
    pass
else:
    print("IOError not raised")
print(repr(decomp.decompress(bz2.compress(b"123"))))
print(repr(decomp.decompress(bz2.compress(b"x" * 1000))))
print(decomp.eof)
print(repr(decomp.decompress()))
print(decomp.eof)
print(repr(decomp.decompress(b"not bzipped data")))
print(decomp.eof)
print()
# Test the open() interface.

# Test the simple read-only file interface.
with bz2.open(TESTFN, "rt") as f:
