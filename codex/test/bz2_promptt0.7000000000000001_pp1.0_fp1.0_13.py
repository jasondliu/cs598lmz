import bz2
# Test BZ2Decompressor.decompress
# Decompress a compressed string.

# Small compressed strings should be decompressed in one call.

decompressor = bz2.BZ2Decompressor()
assert decompressor.decompress(bz2.compress(b"small")) == b"small"
assert decompressor.unused_data == b""

decompressor = bz2.BZ2Decompressor()
assert decompressor.decompress(bz2.compress(b"another small string")) == b"another small string"
assert decompressor.unused_data == b""

# If a compressed string is larger than the decompressor's "unconsumed_tail",
# it should be decompressed in two calls.

decompressor = bz2.BZ2Decompressor()
assert decompressor.decompress(bz2.compress(b"a string longer than the unconsumed_tail")) == b"a string longer than the unconsumed_tail"
assert decompressor.unused_data == b""

