import lzma
# Test LZMADecompressor
comp = lzma.LZMACompressor()

assert lzma.LZMADecompressor().decompress(b'') == b''
assert lzma.LZMADecompressor().decompress(b'x' * 100000) == b'x' * 100000

data_1 = b'abcd' * 100000
data_2 = comp.compress(data_1)
data_2 += comp.flush()
ddata = lzma.LZMADecompressor().decompress(data_2)
assert ddata == data_1

data_1 = b'abcd' * 100000
data_2 = comp.compress(data_1)
data_2 += comp.flush()
lz = lzma.LZMADecompressor()
ddata = lz.decompress(data_2)
ddata = lz.decompress(data_2)
assert ddata == b''

# Issue #10392: Issue with lzma.decompress()
data = comp.compress
