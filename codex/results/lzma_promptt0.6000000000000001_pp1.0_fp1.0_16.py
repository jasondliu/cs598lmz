import lzma
# Test LZMADecompressor
# https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor

# Test 1
d = lzma.LZMADecompressor()
result = d.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6B\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x00\x00\xc4\xa8p\x1b')
print(result)

# Test 2
d = lzma.LZMADecompressor()
result = d.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6B\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x00\x00\xc4\xa8p\x1b')
print(result)

# Test 3
