import bz2
# Test BZ2Decompressor with partial feeds and a get_read_size equal to the
# file size.
comp = bz2.BZ2Decompressor()
