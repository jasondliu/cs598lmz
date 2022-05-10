import lzma
# Test LZMADecompressor
inp = lzma.LZMADecompressor()
print(inp.decompress(compressed).decode('utf-8'))

compressed = lzma.compress(b'Body bilder')
print(compressed)

decomp = lzma.decompress(compressed)
print(decomp)

compressed = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x80\x00\x00\x07\x00'
print(lzma.decompress(compressed))
