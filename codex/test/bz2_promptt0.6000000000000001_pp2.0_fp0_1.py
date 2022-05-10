import bz2
# Test BZ2Decompressor.decompress() with a small buffer size
# to test the code path that processes data in multiple chunks.
# This is important because the bz2 module is used to decompress
# log files, which are usually large and therefore must be processed
# in chunks.

# decompress() should return the empty string when no more data is available

decomp = bz2.BZ2Decompressor()
assert decomp.decompress(b'') == b''

# decompress() should raise an exception if the compressed data is truncated

