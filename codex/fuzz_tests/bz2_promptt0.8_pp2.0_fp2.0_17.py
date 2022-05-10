import bz2
# Test BZ2Decompressor.decompress()

# Test decompressing normal data
decompressor = bz2.BZ2Decompressor()
assert decompressor.decompress(bz2.compress(b"test")) == b"test"

# Test decompressing empty string
assert decompressor.decompress(bz2.compress(b"")) == b""

# Test decompressing single-byte string
assert [decompressor.decompress(bz2.compress(bytes([i])))
        for i in range(256)] == [bytes([i]) for i in range(256)]

# Test decompressing some data incrementally
decompressor = bz2.BZ2Decompressor()
assert decompressor.decompress(bz2.compress(b"test")[:3]) == b""
assert decompressor.decompress(bz2.compress(b"test")[3:]) == b"test"

# Test decompressing uninitialized
decompressor = bz2.BZ2Decompressor()
try:
    decompressor.decompress
