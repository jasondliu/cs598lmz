import lzma
# Test LZMADecompressor, LZMAEncoder, LZMACompressor and LZMADecoder objects.

# Decompressor

# test decompressor with input from BytesIO
decompressor = lzma.LZMADecompressor()
assert decompressor.decompress(b"") == b""
