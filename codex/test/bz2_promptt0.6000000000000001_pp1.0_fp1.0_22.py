import bz2
# Test BZ2Decompressor.flush()

# Test that flush() returns an empty bytes object if there is no data to flush
d = bz2.BZ2Decompressor()
