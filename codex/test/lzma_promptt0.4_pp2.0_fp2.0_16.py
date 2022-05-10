import lzma
# Test LZMADecompressor with a small input

d = lzma.LZMADecompressor()

inp = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'

# Input must be a multiple of 4 bytes
