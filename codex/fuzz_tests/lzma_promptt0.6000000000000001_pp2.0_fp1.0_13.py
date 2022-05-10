import lzma
# Test LZMADecompressor.decompress()

data = b"x" * 100000 + b"y" * 1000
comp = lzma.LZMACompressor()

# Compress and decompress in one step
assert lzma.decompress(comp.compress(data)) == data

# Compress and decompress in multiple steps
cdata = comp.compress(data)
d = lzma.LZMADecompressor()
buf = d.decompress(cdata)
assert buf == data[:len(buf)]
buf = d.decompress(cdata[len(buf):])
assert buf == data[len(buf):len(buf)+len(buf)]
buf = d.decompress(cdata[len(buf):])
assert buf == data[len(buf):]

# Test LZMADecompressor.flush()
buf = d.flush()
assert buf == b""

# Test LZMADecompressor.unused_data
assert d.unused_data == b""

# Test LZMADecompressor.e
