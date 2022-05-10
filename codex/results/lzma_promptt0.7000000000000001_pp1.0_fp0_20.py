import lzma
# Test LZMADecompressor
lzc = lzma.LZMADecompressor()
result = lzc.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')
print(result)
# b'hello world\n'
lzc = lzma.LZMADecompressor()
result = lzc.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')
print(result)
# b'hello world\n'

# Test decompressor with multiple concatenated streams
lzc = lzma.LZMADecompressor()
result = lzc.decompress(b'
