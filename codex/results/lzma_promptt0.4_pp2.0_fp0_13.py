import lzma
# Test LZMADecompressor
compressor = lzma.LZMACompressor()
decompressor = lzma.LZMADecompressor()
data = b'The quick brown fox jumps over the lazy dog.'
compressed = compressor.compress(data)
decompressed = decompressor.decompress(compressed)
print(decompressed)

# Test LZMADecompressor.flush()
compressor = lzma.LZMACompressor()
decompressor = lzma.LZMADecompressor()
data = b'The quick brown fox jumps over the lazy dog.'
compressed = compressor.compress(data)
compressed += compressor.flush()
decompressed = decompressor.decompress(compressed)
print(decompressed)
