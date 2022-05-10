import bz2
# Test BZ2Decompressor()
data = b'this is DEFLATE compressed text.'
comp = bz2.BZ2Compressor()
t = comp.compress(data)
t += comp.flush()

decomp = bz2.BZ2Decompressor()
decomp.decompress(t)  # b'this is DEFLATE compressed text.'

