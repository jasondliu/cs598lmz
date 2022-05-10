import lzma
# Test LZMADecompressor
with open('test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    data = f.read()
    result = decompressor.decompress(data)
    print(result)

# Test LZMADecompressor with multiple chunks
with open('test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    data = f.read(100)
    result = decompressor.decompress(data)
    print(result)
    data = f.read()
