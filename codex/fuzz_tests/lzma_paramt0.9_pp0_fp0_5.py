from lzma import LZMADecompressor
LZMADecompressor.decompress(data)
# b'This text is LZMA-compressed.'

# How to determine decompressed size
decompressor = LZMADecompressor()
decompressor.decompress(data[:17], max_length=3)
# b'This'
decompressor.unused_data
# b' text is LZMA-compressed.'

# How to use a preset
decompressor = LZMADecompressor(format=FORMAT_RAW, preset=9 | LZMA_PRESET_EXTREME)
uncompressed_data = decompressor.decompress(compressed_data)
# b'This text is LZMA-compressed. This text is LZMA-compressed.'

# How to create a streaming decompressor
decompressor = LZMADecompressor()
decompressor.decompress(data[:17], max_length=3)
# b'This'
decompressor.unused_data
# b' text is LZMA-compressed.'

# Decompress the remainder
