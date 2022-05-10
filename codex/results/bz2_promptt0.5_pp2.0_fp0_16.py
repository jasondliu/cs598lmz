import bz2
# Test BZ2Decompressor

# Test decompress()

decompressor = bz2.BZ2Decompressor()

assert decompressor.decompress(b"BZh9") == b"foo"
assert decompressor.decompress(b"BZh9") == b""
assert decompressor.decompress(b"BZh9") == b""
assert decompressor.decompress(b"BZh9") == b""

decompressor = bz2.BZ2Decompressor()

assert decompressor.decompress(b"BZh9") == b"foo"
assert decompressor.unused_data == b""
assert decompressor.decompress(b"BZh9") == b""
assert decompressor.unused_data == b""
assert decompressor.decompress(b"BZh9") == b""
assert decompressor.unused_data == b""
assert decompressor.decompress(b"BZh9") == b""
assert decompressor.unused_data == b""

decompressor = bz2
