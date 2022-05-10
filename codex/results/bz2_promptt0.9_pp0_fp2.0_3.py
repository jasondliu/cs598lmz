import bz2
# Test BZ2Decompressor with buffer size larger than internal processing
# buffer.
data = bz2.compress(
