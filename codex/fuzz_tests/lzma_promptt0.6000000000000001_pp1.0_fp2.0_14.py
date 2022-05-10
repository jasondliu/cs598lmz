import lzma
# Test LZMADecompressor
lzc = lzma.LZMADecompressor()
data = lzc.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')
print(data)
# Test LZMADecompressor.decompress(data)
lzc = lzma.LZMADecompressor()
data = lzc.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')
print(data)

# Test LZMADecompressor.decompress(data, max_length)
lzc = lzma.LZMADecompressor()
data = l
