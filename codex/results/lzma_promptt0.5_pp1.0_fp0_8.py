import lzma
# Test LZMADecompressor:

# data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
#
# decompressor = lzma.LZMADecompressor()
#
# result = decompressor.decompress(data)
# print(result)
#
# result += decompressor.flush()
#
# print(result)

# Test LZMACompressor:

data = b'Hello World!\n'
compressor = lzma.LZMACompressor()
result = compressor.compress(data)
print(result)

result += compressor.flush()

print(result)
