import bz2
# Test BZ2Decompressor with multiple close() calls.
import bz2
decomp = bz2.BZ2Decompressor()
d = decomp.decompress(bz2.compress(b'x' * 10))
