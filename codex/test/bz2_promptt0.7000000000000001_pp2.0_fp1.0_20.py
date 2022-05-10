import bz2
# Test BZ2Decompressor.read with a large buffer size
# to make sure it doesn't return a short buffer
d = bz2.BZ2Decompressor()
