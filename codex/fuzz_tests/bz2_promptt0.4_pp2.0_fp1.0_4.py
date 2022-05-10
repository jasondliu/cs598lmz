import bz2
# Test BZ2Decompressor

# Test decompressor.decompress()
decompressor = bz2.BZ2Decompressor()
assert decompressor.decompress(b"BZh91AY&SY") == b"hello"

# Test decompressor.decompress() with extra data
decompressor = bz2.BZ2Decompressor()
assert decompressor.decompress(b"BZh91AY&SYhIx") == b"hello"

# Test decompressor.decompress() with multiple calls
decompressor = bz2.BZ2Decompressor()
assert decompressor.decompress(b"BZh") == b""
assert decompressor.decompress(b"91AY&SY") == b"hello"

# Test decompressor.flush()
decompressor = bz2.BZ2Decompressor()
assert decompressor.decompress(b"BZh91AY&SY") == b"hello"
assert decompressor.flush() == b""

# Test decompressor.flush() with extra data
decompressor = bz2
