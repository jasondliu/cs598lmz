import lzma
# Test LZMADecompressor directly.
d = lzma.LZMADecompressor()
data = b'\x00\x00\x00\x01\x00!\x9c\xdbW\x01\xc0\xaf,!\x00\x00\x00\x04'
