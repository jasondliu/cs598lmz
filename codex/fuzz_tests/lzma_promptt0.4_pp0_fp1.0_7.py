import lzma
# Test LZMADecompressor with a custom dictionary.

data = b'abcdefghijklmnopqrstuvwxyz' * 100

# Compress with a custom dictionary.
compressor = lzma.LZMACompressor(dict_size=len(data))
compressed = compressor.compress(data)
compressed += compressor.flush()

# Decompress with a custom dictionary.
decompressor = lzma.LZMADecompressor(dict_size=len(data))
decompressed = decompressor.decompress(compressed)

print(decompressed == data)
