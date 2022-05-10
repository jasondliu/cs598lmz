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
ret += d.decompress(b"bar")
ret += d.decompress(b"")
ret += d.decompress(b"spam")
ret += d.decompress(b"eggs")
ret += d.decompress(b"")
print(ret)

# Test LZMADecompressor.decompress() with multiple buffers
d = lzma.LZMADecompressor()
ret = d.decompress(b"foo")
ret += d.decompress(b"bar", max_length=1)
ret += d.decompress(b"baz", max_
