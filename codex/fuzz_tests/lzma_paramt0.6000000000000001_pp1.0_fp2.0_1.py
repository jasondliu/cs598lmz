from lzma import LZMADecompressor
LZMADecompressor.decompress(s)

# Decompress with a larger dictionary
LZMADecompressor(dict_size=2**30).decompress(s)

# Decompress with a preset dictionary
LZMADecompressor(dict_size=2**30, preset=3).decompress(s)

# Decompress asynchronously
decompressor = LZMADecompressor(dict_size=2**30)
decompressor.decompress(s[:100])
decompressor.decompress(s[100:])
decompressor.decompress(b'', True)

# Decompress asynchronously with a preset dictionary
decompressor = LZMADecompressor(dict_size=2**30, preset=3)
decompressor.decompress(s[:100])
decompressor.decompress(s[100:])
decompressor.decompress(b'', True)
