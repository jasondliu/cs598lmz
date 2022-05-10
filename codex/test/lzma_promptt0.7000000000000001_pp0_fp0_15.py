import lzma
# Test LZMADecompressor.
for size in [0, 1, 7, 8, 9, 15, 16, 17, 100]:
    data = b'x' * size
    cdata = lzma.compress(data)
    d = lzma.LZMADecompressor()
