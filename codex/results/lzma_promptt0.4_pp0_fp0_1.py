import lzma
# Test LZMADecompressor.

# Decompress data from a file.
with lzma.open('example.xz', 'rb') as f:
    file_content = f.read()

# Decompress data from a stream.
compressed = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'
decompressor = lzma.LZMADecompressor()
result = decompressor.decompress(compressed)

# Decompress data with a known uncompressed size.
compressed = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'
decompressor = lzma.LZMADecompressor()
result = decompressor
