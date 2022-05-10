import lzma
# Test LZMADecompressor

data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'

c = lzma.LZMADecompressor()

print(c.decompress(data))
print(c.unused_data)

# Test LZMADecompressor.decompress() with multiple calls

c = lzma.LZMADecompressor()

print(c.decompress(data[:10]))
print(c.decompress(data[10:]))
print(c.unused_data)

# Test LZMADecompressor.decompress() with multiple calls,
# including a call with unused_data

c = lzma.LZMADecompressor()

print(c.decompress(data[:7]))
print(c.decompress(data[7:]
