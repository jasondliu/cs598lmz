from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

# b'Hello World!Hello World!Hello World!Hello World!'

# Compress the data with LZMA compression
compressed = LZMACompressor().compress(data)
compressed

# b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xcaIU\x01\x00\x00\x04\x00\x00\x00'

# Decompress the data with LZMA compression
LZMADecompressor().decompress(compressed)

# b'Hello World!Hello World!Hello World!Hello World!'

# Compress the data with BZ2 compression
compressed = BZ2Compressor().compress(data)
compressed

# b'BZh91AY&SY\xe4b\x00\x00\x00\x01\x01\x80@\x00 \x00!\x
