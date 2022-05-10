import lzma
# Test LZMADecompressor
# print(lzma.decompress(lzma.compress(b'Hello World')))

# Test LZMACompressor
compressor = lzma.LZMACompressor(lzma.FORMAT_XZ)
print(compressor.compress(b'Hello World'))
print(compressor.flush())

# Test LZMADecompressor
decompressor = lzma.LZMADecompressor(lzma.FORMAT_XZ)
print(decompressor.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x00\x00\x04'))

