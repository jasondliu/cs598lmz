import lzma
# Test LZMADecompressor and LZMACompressor

# Test LZMADecompressor

decompressor = lzma.LZMADecompressor()

# Test LZMADecompressor.decompress()

# Test LZMADecompressor.decompress(b'')
assert decompressor.decompress(b'') == b''

# Test LZMADecompressor.decompress(b'x')
