import lzma
# Test LZMADecompressor with a small data
d = lzma.LZMADecompressor()
d.decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00\x21\x01\x1c\x00\x00\x00')
# Test LZMADecompressor with a large data
d = lzma.LZMADecompressor()
d.decompress(open('../src/samples/lzma/lzma.xz', 'rb').read())
# Test LZMADecompressor.flush()
data = open('../src/samples/lzma/lzma.xz', 'rb').read()
d = lzma.LZMADecompressor()
d.decompress(data[:-10])
d.flush()
d.decompress(data[-10:])
# Test LZMADecompressor with a truncated data
d = l
