from lzma import LZMADecompressor
LZMADecompressor()

# The compressed data is a byte array
compressed = b'...'

# Decompress the data
decompressed = LZMADecompressor().decompress(compressed)

# The variable 'decompressed' contains the decompressed data
# ...

# When the compressed data is no longer needed, call flush() to free up memory
