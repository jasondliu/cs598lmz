import lzma
# Test LZMADecompressor.
data = lzma.compress(b'1234567890')
d = lzma.LZMADecompressor()
d.decompress(data)

print(d)

