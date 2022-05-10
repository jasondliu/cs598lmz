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
for chunk in [compressed[:4], compressed[4:]]:
    decompressed += decompressor.decompress(compressed)
    if decompressor.unused_data:
        chunks.append(decompressor.unused_data)
print(decompressed)
print(chunks)

# Decompress data with a different buffer size
decompressor = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)
decompressed = b""
stream_ch
