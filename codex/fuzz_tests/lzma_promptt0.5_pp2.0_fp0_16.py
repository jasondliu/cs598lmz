import lzma
# Test LZMADecompressor.decompress() with a large buffer size

# Use a small buffer size and a small dictionary size to make
# the test run faster.
decompressor = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE,
                                     filters=[{"id": lzma.FILTER_LZMA2,
                                               "dict_size": 2 ** 20}])

# This should decompress to a single "a" character.
compressed = b"\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00\x00"

# Use a large buffer size to make sure the decompressor can handle
# it.
data = decompressor.decompress(compressed, 2 ** 20)
assert data == b"a"
assert decompressor.unused_data == b""
assert decompressor.eof
# Test LZMADecompressor
