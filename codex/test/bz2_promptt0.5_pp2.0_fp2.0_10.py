import bz2
# Test BZ2Decompressor
bz2_comp = bz2.BZ2Compressor()
bz2_decomp = bz2.BZ2Decompressor()
bz2_comp.compress(b"Hello World!")

bz2_comp.flush()

