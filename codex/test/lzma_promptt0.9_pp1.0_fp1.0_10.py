import lzma
# Test LZMADecompressor.decompress
data = b'sixteen ' * 16 + b'X' * 100
cdata = lzma.compress(data)
assert lzma.decompress(cdata) == data

d = lzma.LZMADecompressor()
assert d.decompress(cdata) == data
