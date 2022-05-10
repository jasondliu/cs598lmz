import bz2
# Test BZ2Decompressor.read()

# Test different read sizes
decomp = bz2.BZ2Decompressor()
data = bz2.compress(b"foo" * 100)
