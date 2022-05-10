import bz2
# Test BZ2Decompressor with multiple concatenated streams

data = bz2.BZ2Compressor().compress(b'foo')
data += bz2.BZ2Compressor().compress(b'bar')
data += bz2.BZ2Compressor().flush()

d = bz2.BZ2Decompressor()
