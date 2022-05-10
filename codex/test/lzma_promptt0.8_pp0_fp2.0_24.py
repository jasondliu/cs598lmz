import lzma
# Test LZMADecompressor.read()

compressed = lzma.compress(b"this is a test")

decompressor = lzma.LZMADecompressor()

data = decompressor.decompress(compressed)
print(data)

