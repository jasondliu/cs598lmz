import lzma
# Test LZMADecompressor
c = lzma.LZMACompressor()
ret = c.compress(b"foo")
ret += c.flush()
d = lzma.LZMADecompressor()
print(d.decompress(ret))

# Test LZMADecompressor.decompress() with buffers
d = lzma.LZMADecompressor()
ret = d.decompress(b"foo")
