import lzma
# Test LZMADecompressor

compressor = lzma.LZMACompressor()
compressed = compressor.compress(b"foo")
compressed += compressor.flush()
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
decompressed += decompressor.flush()
print(decompressed)

# Test LZMADecompressor.decompress()

compressor = lzma.LZMACompressor()
compressed = compressor.compress(b"foo")
compressed += compressor.flush()
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
decompressed += decompressor.flush()
print(decompressed)

# Test LZMADecompressor.decompress()

compressor = lzma.LZMACompressor()
compressed = compressor.compress(b"foo")
compressed += compressor.flush()
decompressor = lzma.LZMADecompressor()

