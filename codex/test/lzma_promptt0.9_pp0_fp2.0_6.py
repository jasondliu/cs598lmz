import lzma
# Test LZMADecompressor() instances functionality.
decomp = lzma.LZMADecompressor()
b = memoryview(bytearray(1))
decomp.decompress(b, 0)

# Test LZMACompressor() instances functionality.
comp = lzma.LZMACompressor()
comp.compress(b)
comp.flush()
# Run the test suite.
