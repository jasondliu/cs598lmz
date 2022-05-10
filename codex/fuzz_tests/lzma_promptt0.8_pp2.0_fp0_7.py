import lzma
# Test LZMADecompressor.eof
b = lzma.compress(b'text')
d = lzma.LZMADecompressor()
d.decompress(b[:1])
assert not d.eof
d.decompress(b[1:])
assert d.eof
try:
    d.decompress(b'text')
except EOFError:
    pass
else:
    raise Exception

# Test LZMADecompressor.unused_data
d = lzma.LZMADecompressor()
d.decompress(b[:1])
assert d.unused_data == b[1:]
d.decompress(b[1:])
assert d.unused_data == b''

# Test LZMADecompressor.decompress with max_length
d = lzma.LZMADecompressor()
assert d.decompress(b, max_length=2) == b'te'
d.decompress(b[2:])
assert d.unused_data == b
