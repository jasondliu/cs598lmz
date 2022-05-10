import lzma
# Test LZMADecompressor object.
c = lzma.LZMACompressor()
compressed = c.compress(b'1234567890abcdefgh')
print(compressed)

c.flush()
