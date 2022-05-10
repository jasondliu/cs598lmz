import lzma
# Test LZMADecompressor

# Decompress
decompressor = lzma.LZMADecompressor()
data = decompressor.decompress(lzma_data)

# Test LZMACompressor

# Compress
compressor = lzma.LZMACompressor()
lzma_data = compressor.compress(data)
lzma_data += compressor.flush()

# Decompress
decompressor = lzma.LZMADecompressor()
data = decompressor.decompress(lzma_data)

# Test LZMADecompressor.seek()

# Decompress
decompressor = lzma.LZMADecompressor()
data = decompressor.decompress(lzma_data)

# Seek
decompressor.seek(0)
data = decompressor.decompress(lzma_data)

# Test LZMADecompressor.unused_data

# Decompress
decompressor = lzma.LZMADecompressor()
data = decomp
