import lzma
# Test LZMADecompressor
data = b'this is the original data'

cdata = lzma.compress(data)
print(len(data), len(cdata))

d = lzma.LZMADecompressor()
print(d.decompress(cdata))

