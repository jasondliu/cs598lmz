import lzma
# Test LZMADecompressor

# Compress data
data = b"Hello, World!" * 100
compressor = lzma.LZMACompressor()
compressed = compressor.compress(data)
compressed += compressor.flush()

# Decompress data
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
print(decompressed)

# Decompress data incrementally
decompressor = lzma.LZMADecompressor()
chunks = []
decompressed = b""
