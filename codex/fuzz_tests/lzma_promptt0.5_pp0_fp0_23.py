import lzma
# Test LZMADecompressor

# Compress data
compressor = lzma.LZMACompressor()
data = b"".join(compressor.compress(line) for line in open("/etc/passwd"))
data += compressor.flush()

# Decompress data
decompressor = lzma.LZMADecompressor()
decompressed_data = b"".join(decompressor.decompress(data))
print(decompressed_data)

# Decompress data with a filter chain
decompressor = lzma.LZMADecompressor(lzma.FORMAT_RAW, None, lzma.FILTER_LZMA1)
decompressed_data = b"".join(decompressor.decompress(data))
print(decompressed_data)

# Decompress data with a preset filter chain
decompressor = lzma.LZMADecompressor(lzma.FORMAT_XZ, preset=9)
decompressed_data = b"".join(decompressor.decompress(data))
