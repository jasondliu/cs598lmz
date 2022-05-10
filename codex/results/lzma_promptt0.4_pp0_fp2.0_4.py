import lzma
# Test LZMADecompressor

print('Test LZMADecompressor')

print('Test decompress()')
d = lzma.LZMADecompressor()
data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x80\x04\x00\x00\x00\x00'
decompressed = d.decompress(data)
print(decompressed)

print('Test decompress() with max_length')
d = lzma.LZMADecompressor()
data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x80\x04\x00\x00\x00\x00'
decompressed = d.decompress(data, max_length=10)
print(dec
