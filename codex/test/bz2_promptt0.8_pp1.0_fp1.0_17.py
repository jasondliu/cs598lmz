import bz2
# Test BZ2Decompressor's built-in read()
comp = bz2.BZ2Compressor()
b1 = comp.compress(b"foo")
b2 = comp.compress(b"bar")
b3 = comp.flush()
data = b1 + b2 + b3

dc = bz2.BZ2Decompressor()
result = dc.decompress(data)
