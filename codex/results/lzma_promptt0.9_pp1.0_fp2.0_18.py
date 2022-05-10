import lzma
# Test LZMADecompressor
c = lzma.LZMADecompressor()
data = b('', 'latin')
assert c.decompress(data) == b('')
#
c = lzma.LZMADecompressor()
c.decompress(data, max_length=0)
c.decompress(data, max_length=0, max_length=0)
c = lzma.LZMADecompressor()
data = lzma.compress(b('x'*10, 'latin'))
assert c.decompress(data) == b('x'*10)
#
c = lzma.LZMADecompressor()
data = lzma.compress(b('x'*10, 'latin'))
assert c.decompress(data, max_length=5) == b('x'*5)
#
c = lzma.LZMADecompressor()
data = lzma.compress(b('x'*10, 'latin'))
assert c.decomp
