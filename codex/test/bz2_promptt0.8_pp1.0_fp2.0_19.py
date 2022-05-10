import bz2
# Test BZ2Decompressor with a small decompress buffer
# This tests that we don't lose any parts of the stream after a short decompress
# buffer.
data = b"\xc5\x04\x00\x00\x00\x00\x00\x01"
# decompress with a short decompress buffer
bz = bz2.BZ2Decompressor()
