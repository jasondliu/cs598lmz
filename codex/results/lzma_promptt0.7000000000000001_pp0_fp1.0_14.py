import lzma
# Test LZMADecompressor, LZMAEncoder, LZMACompressor and LZMADecoder objects.

# Decompressor

# test decompressor with input from BytesIO
decompressor = lzma.LZMADecompressor()
assert decompressor.decompress(b"") == b""
assert decompressor.decompress(b"test") == b"test"
assert decompressor.decompress(b"test" * 100) == b"test" * 100

# test decompressor with fileobj
file = BytesIO(b"test")
decompressor = lzma.LZMADecompressor()
assert decompressor.decompress(file) == b"test"

# test decompressor with max_length
file = BytesIO(b"test" * 100)
decompressor = lzma.LZMADecompressor()
assert decompressor.decompress(file, max_length=4) == b"test"

# test decompressor with multiple calls to decompress
file = BytesIO(b"test" * 100)
dec
