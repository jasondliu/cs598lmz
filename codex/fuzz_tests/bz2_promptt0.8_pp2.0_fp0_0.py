import bz2
# Test BZ2Decompressor with multiple close() calls.
import bz2
decomp = bz2.BZ2Decompressor()
d = decomp.decompress(bz2.compress(b'x' * 10))
decomp.close()
decomp.close()
# Test BZ2Compressor with multiple close() calls.
bz2.compress(b'x' * 10)
comp = bz2.BZ2Compressor()
comp.compress(b'x' * 10)
comp.close()
comp.close()
