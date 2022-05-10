import lzma
# Test LZMADecompressor on a file that was compressed with LZMA-JS
f = open('test.lzma', 'rb')
d = lzma.LZMADecompressor()
data = d.decompress(f.read())
print(data)

# Test LZMADecompressor on a file that was compressed with LZMA-SDK
f = open('test.lzma_sdk', 'rb')
d = lzma.LZMADecompressor()
data = d.decompress(f.read())
print(data)

# Test LZMADecompressor on a file that was compressed with LZMA-SDK
# and has a filter chain
f = open('test.lzma_sdk_filters', 'rb')
d = lzma.LZMADecompressor()
data = d.decompress(f.read())
print(data)

# Test LZMADecompressor on a file that was compressed with LZMA-SDK
# and has a filter chain with a non-default dict_size
