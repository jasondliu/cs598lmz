import lzma
# Test LZMADecompressor.eof.

data = list(range(10000))
comp = lzma.LZMACompressor()
