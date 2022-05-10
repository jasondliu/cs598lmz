import lzma
# Test LZMADecompressor

# The following is a test from the Python documentation

comp = lzma.LZMACompressor()
data = b"".join(comp.compress(bytes(i)) for i in range(1000))
data += comp.flush()

decomp = lzma.LZMADecompressor()
decomp.decompress(data)

# The following is a test from the XZ Utils documentation

data = b"".join(bytes(i) for i in range(1000))

comp = lzma.LZMACompressor()
comp.compress(data)
comp.compress(b"")
comp.compress(data)
comp.compress(b"")
comp.compress(data)
comp.compress(b"")
comp.compress(data)
comp.compress(b"")
comp.compress(data)
comp.compress(b"")
comp.compress(data)
comp.compress(b"")
comp.compress(data)
comp.compress(b"")
