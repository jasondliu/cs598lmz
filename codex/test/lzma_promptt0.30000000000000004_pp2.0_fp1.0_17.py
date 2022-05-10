import lzma
# Test LZMADecompressor

# Compress a string
compressed = lzma.compress(b'Hello World!')

# Decompress a string
decompressed = lzma.decompress(compressed)

print(decompressed)

# Decompress a file
