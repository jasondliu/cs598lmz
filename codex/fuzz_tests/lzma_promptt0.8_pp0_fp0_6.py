import lzma
# Test LZMADecompressor class
src = b'This is the data to be compressed'
dc = lzma.LZMADecompressor()
d = dc.decompress(src)

c = lzma.LZMACompressor()
src = b'This is the data to be compressed'
d = c.compress(src)
d += c.flush()  
print(src)
print(d)

src = b'This is the data to be compressed'
dc = lzma.LZMADecompressor()
d = dc.decompress(d)
print(d)

# Test LZMADecompressor iterable
src = b'This is the data to be compressed'
dc = lzma.LZMADecompressor()
d = dc.decompress(src)

c = lzma.LZMACompressor()
src = b'This is the data to be compressed'
d = c.compress(src)
d += c.flush()  
print(src)
print(d)

src = b'This is the
