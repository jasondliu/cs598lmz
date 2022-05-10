import bz2
# Test BZ2Decompressor.eof for a file which has an odd number of nulls

data = bz2.BZ2Compressor().compress(b"\0" * 3)
data += bz2.compress(b"x")

decomp = bz2.BZ2Decompressor()
