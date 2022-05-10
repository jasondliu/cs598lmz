import lzma
# Test LZMADecompressor

print('Test LZMADecompressor')

print('Test decompress()')
d = lzma.LZMADecompressor()
data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x80\x04\x00\x00\x00\x00'
