from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# Compress data
compressor = LZMACompressor()
compressed_data = compressor.compress(data)
compressed_data += compressor.flush()

# Decompress data
decompressor = LZMADecompressor()
decompressed_data = decompressor.decompress(compressed_data)

# Compress data using a preset compression level
compressor = LZMACompressor(preset=9 | LZMA_PRESET_EXTREME)
compressed_data = compressor.compress(data)
compressed_data += compressor.flush()

# Decompress data using a preset compression level
decompressor = LZMADecompressor(preset=9 | LZMA_PRESET_EXTREME)
decompressed_data = decompressor.decompress(compressed_data)

# Compress data using a dictionary
compressor = LZMACompressor(dict_size=1 << 23)
compressed_data = compressor.compress(data)
compressed_data += compressor.flush()

