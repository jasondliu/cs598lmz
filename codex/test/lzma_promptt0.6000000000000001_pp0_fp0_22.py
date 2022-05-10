import lzma
# Test LZMADecompressor class

# Compress some data
c = lzma.LZMACompressor()
data = b"Test data"
compressed = c.compress(data)

# Decompress the data
d = lzma.LZMADecompressor()
print(d.decompress(compressed))

# Decompress the data in chunks
d = lzma.LZMADecompressor()
decompressed = b""
