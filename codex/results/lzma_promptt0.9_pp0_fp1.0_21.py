import lzma
# Test LZMADecompressor with empty data.

decompr = lzma.LZMADecompressor()
data = bytearray()
decompr.decompress(data);
