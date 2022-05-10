import lzma
# Test LZMADecompressor.

# Create a compressed stream
comp = lzma.LZMACompressor()
data = comp.compress(b"Hello") + comp.flush()
print(data)

# Decompress the stream
decomp = lzma.LZMADecompressor()
decomp.decompress(data)

# The LZMADecompressor object has some useful attributes.
# For example, the amount of input data read so far.
print(decomp.unused_data)
print(decomp.eof)

# The LZMADecompressor object can be used as a context manager.
