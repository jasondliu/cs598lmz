import lzma
# Test LZMADecompressor.decompress
data = b'sixteen ' * 16 + b'X' * 100
cdata = lzma.compress(data)
assert lzma.decompress(cdata) == data

d = lzma.LZMADecompressor()
assert d.decompress(cdata) == data
assert d.decompress(cdata) == b''
assert d.unused_data == b''
# Test LZMADecompressor.decompress
d = lzma.LZMADecompressor()
assert d.decompress(cdata) == data

d.decompress(b'DATA')
assert d.unused_data == b'DATA'
# Test iterative decompression
d = lzma.LZMADecompressor()
cdata = iter(lzma.compress(data, check=-1))

d2 = lzma.LZMADecompressor()
assert d2.decompress(b''.join(cdata)) == d.decompress(b''.join(c
