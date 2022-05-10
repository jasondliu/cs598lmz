import lzma
# Test LZMADecompressor()
compressor = lzma.LZMACompressor()
decompressor = lzma.LZMADecompressor()
data = b'abcdefghijklmnopqrstuvwxyz'
compressed = compressor.compress(data)
compressed += compressor.flush()
assert decompressor.decompress(compressed) == b'abcdefghijklmnopqrstuvwxyz'
# Test LZMADecompressor.decompress()
compressor = lzma.LZMACompressor()
decompressor = lzma.LZMADecompressor()
data = b'abcdefghijklmnopqrstuvwxyz'
compressed = compressor.compress(data)
compressed += compressor.flush()
assert decompressor.decompress(compressed) == b'abcdefghijklmnopqrstuvwxyz'
# Test LZMADecompressor.unused_data
compressor = lzma.LZMACompressor()
