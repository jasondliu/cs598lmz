import lzma
# Test LZMADecompressor

# Compress
compressor = lzma.LZMACompressor()
compressed = compressor.compress(b"Hello World!")
compressed += compressor.flush()

# Decompress
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
print(decompressed)

# Decompress with context manager
