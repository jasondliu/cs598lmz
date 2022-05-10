import lzma
# Test LZMADecompressor
compressor = lzma.LZMACompressor()
data = b"This is a test"
compressed = compressor.compress(data)
compressed += compressor.flush()
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
decompressed += decompressor.flush()
print(decompressed)

# Test LZMADecompressor with a preset
compressor = lzma.LZMACompressor(preset=9 | lzma.PRESET_EXTREME)
data = b"This is a test"
compressed = compressor.compress(data)
compressed += compressor.flush()
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
decompressed += decompressor.flush()
print(decompressed)

# Test LZMADecompressor with a preset and a filter chain
compressor = lzma.LZMACompressor(filters=[{"id": lzma.
