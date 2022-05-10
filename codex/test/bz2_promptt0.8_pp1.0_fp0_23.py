import bz2
# Test BZ2Decompressor.flush()
decomp = bz2.BZ2Decompressor()
decomp.decompress(b'BZ')
