import lzma
# Test LZMADecompressor.decompress(bytes) and LZMADecompressor.decompress().
d = lzma.LZMADecompressor()
data = d.decompress(b'#\x00\x00\x00\x10\x00\x1b\xb4\x4e\xfc\x85\x20\x0e\x82\xa0\x08')
print(data)
print(d.decompress())       # returns b'' because there is nothing to decompress
