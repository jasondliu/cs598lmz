import bz2
# Test BZ2Decompressor()
data = b'this is DEFLATE compressed text.'
comp = bz2.BZ2Compressor()
t = comp.compress(data)
t += comp.flush()

decomp = bz2.BZ2Decompressor()
decomp.decompress(t)  # b'this is DEFLATE compressed text.'

decomp.decompress(b'this is not bz2 data.')
# Traceback (most recent call last):
#   ...
# BZ2Decompressor.decompress() expects a chunk starting with the BZ2 magic
# numbers.  If you generate compressed output with other BZ2 compressing
# applications, make sure to include the starting magic numbers.

decomp.decompress(data)
# Traceback (most recent call last):
#   ...
# BZ2Decompressor.decompress() failed (-3): BZ_DATA_ERROR_MAGIC
# The second decompress() call above fails since no valid bz2 data is passed
