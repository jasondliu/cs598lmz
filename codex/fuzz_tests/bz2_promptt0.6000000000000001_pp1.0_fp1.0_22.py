import bz2
# Test BZ2Decompressor.flush()

# Test that flush() returns an empty bytes object if there is no data to flush
d = bz2.BZ2Decompressor()
assert d.flush() == b''

# Test that decompressor returns empty bytes if there is no data to flush
# and there is no data available in the buffer
d = bz2.BZ2Decompressor()
assert d.decompress(b'BZh9') == b''

# Test that decompressor returns empty bytes if there is no data to flush
# and the buffer is empty
d = bz2.BZ2Decompressor()
assert d.decompress(b'BZh9') == b''

# Test that decompressor returns empty bytes if there is no data to flush
# and the buffer is not empty
d = bz2.BZ2Decompressor()
assert d.decompress(b'BZh9') == b''

# Test that flush() returns data from the buffer if there is no data to flush
# and there is data available in the buffer
d = bz2.BZ
