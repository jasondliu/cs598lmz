import lzma
# Test LZMADecompressor

compressed = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa4\x81\x00\x00\x0c\xe9\x16\x00\x00\x00\x00'

decomp = lzma.LZMADecompressor()
decomp.decompress(compressed)

# Test LZMADecompressor with multiple calls to decompress()

decomp = lzma.LZMADecompressor()
decomp.decompress(compressed[:10])
decomp.decompress(compressed[10:])

# Test LZMADecompressor.flush()

decomp = lzma.LZMADecompressor()
