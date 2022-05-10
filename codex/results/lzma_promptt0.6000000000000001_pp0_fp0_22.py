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
for chunk in [compressed[:5], compressed[5:], b"end"]:
    decompressed += d.decompress(chunk)

print(decompressed)

# Decompress the data in chunks,
# decompressing the last chunk with a different method
d = lzma.LZMADecompressor()
decompressed = b""
for chunk in [compressed[:5], compressed[5:9], compressed[9:]]:
    decompressed += d.decompress(chunk)

decompressed += d.flush()

print(decompressed)

# Decompress the data
