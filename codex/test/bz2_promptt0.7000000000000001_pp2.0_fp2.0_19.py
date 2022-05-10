import bz2
# Test BZ2Decompressor
data = bz2.BZ2Compressor().compress(b"Hello World!")

d = bz2.BZ2Decompressor()
d.decompress(data)
