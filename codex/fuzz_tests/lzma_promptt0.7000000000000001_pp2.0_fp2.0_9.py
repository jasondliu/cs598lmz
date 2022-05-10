import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
decompressor.decompress(bytes_compressed)

# Test LZMADecompressor with multiple decompress() calls
decompressor = lzma.LZMADecompressor()
decompressor.decompress(bytes_compressed[:100])
decompressor.decompress(bytes_compressed[100:])
decompressor.decompress(b'')

# Test LZMADecompressor "eof" and "unused_data" attributes
decompressor = lzma.LZMADecompressor()
decompressor.decompress(bytes_compressed)
assert decompressor.eof
assert decompressor.unused_data == b''
decompressor = lzma.LZMADecompressor()
decompressor.decompress(bytes_compressed + b'garbage')
assert decompressor.eof
assert decompressor.unused_data == b'garbage'

# Test LZMADecompressor.flush()
