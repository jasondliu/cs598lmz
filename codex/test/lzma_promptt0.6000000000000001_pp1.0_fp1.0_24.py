import lzma
# Test LZMADecompressor
lzc = lzma.LZMADecompressor()
print(lzc.decompress(b'\xfd\x37\x7a\x58\x5a\x00'))

