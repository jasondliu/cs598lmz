import lzma
# Test LZMADecompressor on a string
data = open('test.xz', 'rb').read()
decompressor = lzma.LZMADecompressor()
result = decompressor.decompress(data)
len(result)

# Test LZMADecompressor on a file-like object
data = open('test.xz', 'rb')
decompressor = lzma.LZMADecompressor()
