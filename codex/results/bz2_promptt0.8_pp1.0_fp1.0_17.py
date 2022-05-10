import bz2
# Test BZ2Decompressor's built-in read()
comp = bz2.BZ2Compressor()
b1 = comp.compress(b"foo")
b2 = comp.compress(b"bar")
b3 = comp.flush()
data = b1 + b2 + b3

dc = bz2.BZ2Decompressor()
result = dc.decompress(data)
result += dc.decompress(dc.unused_data)
result += dc.flush()
assert result == b"foobar"

# Test BZ2Decompressor's read1()

data = bz2.compress(b"foobarbaz")

dc = bz2.BZ2Decompressor()
result = dc.decompress(data[:3])
assert result == b"foo"
result = dc.decompress(data[3:10])
assert result == b"barbaz"
result = dc.flush()
assert result == b""
result = dc.decompress(b"")
assert result == b""
result = dc.flush()
assert
