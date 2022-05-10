import lzma
# Test LZMADecompressor.decompress() and LZMADecompressor.flush()
comp = lzma.LZMACompressor()
print(comp.compress(b"foo"))
print(comp.flush())

dec = lzma.LZMADecompressor()
