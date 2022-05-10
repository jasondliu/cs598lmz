import bz2
# Test BZ2Decompressor with a small decompress buffer
# This tests that we don't lose any parts of the stream after a short decompress
# buffer.
data = b"\xc5\x04\x00\x00\x00\x00\x00\x01"
# decompress with a short decompress buffer
bz = bz2.BZ2Decompressor()
decompressed = bz.decompress(data, 4)
# this should return nothing and then complete when a larger buffer is given
assert decompressed <= data and bz.eof
# decompress the rest of the data
decompressed += bz.decompress(b"", 7)
# this should return the whole decompressed stream
assert decompressed == bz2.decompress(data) and bz.eof
