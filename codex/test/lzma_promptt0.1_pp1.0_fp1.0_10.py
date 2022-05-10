import lzma
# Test LZMADecompressor.decompress()

# Test decompression of a single-chunk stream
compressor = lzma.LZMACompressor()
data = b"foo" * 100000
compressed = compressor.compress(data)
compressed += compressor.flush()

decompressor = lzma.LZMADecompressor()
assert decompressor.decompress(compressed) == data

# Test decompression of a multi-chunk stream
compressor = lzma.LZMACompressor()
data = b"foo" * 100000
compressed1 = compressor.compress(data)
compressed2 = compressor.compress(data)
compressed3 = compressor.compress(data)
