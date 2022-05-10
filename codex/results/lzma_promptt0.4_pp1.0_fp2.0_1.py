import lzma
# Test LZMADecompressor

compressed = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'

with lzma.LZMADecompressor() as decompressor:
    # Decompress data
    decompressed = decompressor.decompress(compressed)
    print(decompressed)

# Test LZMADecompressor.decompress() with max_length

compressed = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'

with lzma.LZMADecompressor() as decompressor:
    # Decompress data
    decompressed = decompressor.decompress(compressed, max_length=4)
