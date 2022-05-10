import bz2
# Test BZ2Decompressor.decompress()

# This is a test for Issue #2638

data = bz2.compress(b"hello world")
decomp = bz2.BZ2Decompressor()

# This should raise an exception.
try:
    decomp.decompress(data, 10)
except ValueError:
    pass
else:
    print("Error: expected exception not raised")

# This should return the first 10 bytes of the decompressed data.
s = decomp.decompress(data, 10)
if s != b"hello worl":
    print("Error: expected %r, got %r" % (b"hello worl", s))

# This should return the remainder of the decompressed data.
