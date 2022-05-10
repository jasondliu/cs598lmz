import bz2
# Test BZ2Decompressor with empty input.
# The decoder must return an empty string each time.
comp = bz2.BZ2Compressor()
decomp = bz2.BZ2Decompressor()

# First, feed the compressor with no data.
# Then, feed the decompressor with no data.
# Then, feed the compressor with no data.
# Then, feed the decompressor with no data.
# Etc.
# The decompressor must return an empty string each time.
for i in range(0, 10):
    c = comp.compress(b"")
    assert decomp.decompress(c) == b""
    assert decomp.decompress(b"") == b""

# Test BZ2Compressor + BZ2Decompressor with multiple compress() calls
comp = bz2.BZ2Compressor()
decomp = bz2.BZ2Decompressor()
assert decomp.decompress(comp.compress(b"bla")) == b"bla"
assert decomp.decompress(comp.compress(b"bla")) == b"bl
