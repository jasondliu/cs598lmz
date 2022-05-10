import bz2
# Test BZ2Decompressor.__init__ and .flush()
decompressor = bz2.BZ2Decompressor()
assert decompressor.decompress(b"BZh91AY&SY") == b"this is "
assert decompressor.decompress(b"a magic string") == b"a "
assert decompressor.flush() == b"test"

# Test BZ2Decompressor.__init__ and .decompress() with max_length
decompressor = bz2.BZ2Decompressor()
assert decompressor.decompress(b"BZh91AY&SY") == b"this is "
assert decompressor.decompress(b"a magic string", max_length=4) == b"a "
assert decompressor.decompress(b"a magic string", max_length=9) == b"a magic "
assert decompressor.decompress(b"a magic string", max_length=18) == b"a magic string"
assert decompressor.decompress(b"a magic string", max_length=0) == b""
assert decompressor.
