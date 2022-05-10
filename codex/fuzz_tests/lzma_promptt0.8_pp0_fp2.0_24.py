import lzma
# Test LZMADecompressor.read()

compressed = lzma.compress(b"this is a test")

decompressor = lzma.LZMADecompressor()

data = decompressor.decompress(compressed)
print(data)

data = decompressor.unconsumed_tail
print(data)

data = decompressor.decompress(data)
print(data)

# Test LZMADecompressor.__init__()

decompressor = lzma.LZMADecompressor(lzma.FORMAT_RAW, None, None)

data = decompressor.decompress(compressed)
print(data)

data = decompressor.unconsumed_tail
print(data)

data = decompressor.decompress(data)
print(data)

# Test LZMADecompressor.copy()

copy = decompressor.copy()

data = copy.decompress(compressed)
print(data)

data = copy.unconsumed_tail
print(data)

data =
