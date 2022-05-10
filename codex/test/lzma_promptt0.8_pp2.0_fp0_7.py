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
