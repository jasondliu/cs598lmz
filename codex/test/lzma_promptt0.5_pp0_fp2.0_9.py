import lzma
# Test LZMADecompressor on a file that was compressed with LZMA-JS
f = open('test.lzma', 'rb')
d = lzma.LZMADecompressor()
data = d.decompress(f.read())
print(data)

# Test LZMADecompressor on a file that was compressed with LZMA-SDK
