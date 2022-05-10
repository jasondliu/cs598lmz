import bz2
# Test BZ2Decompressor.incrementaldecompress()

# Issue #2241: crash when calling BZ2Decompressor.decompress() before
# BZ2Decompressor.decompress()
bz2decomp = bz2.BZ2Decompressor()
#try:
#    bz2decomp.decompress(b"")
#except IOError:
#    pass

