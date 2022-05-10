import lzma
# Test LZMADecompressor

compressed = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'

obj = lzma.LZMADecompressor()
data = obj.decompress(compressed)
print(data)

# Test LZMADecompressor with max_length

obj = lzma.LZMADecompressor()
data = obj.decompress(compressed, max_length=6)
print(data)

obj = lzma.LZMADecompressor()
data = obj.decompress(compressed, max_length=7)
print(data)

try:
    obj = lzma.LZMADecompressor()
    data = obj.decompress(compressed, max_length=6, max_length=7)
except TypeError:
    print("TypeError")

try
