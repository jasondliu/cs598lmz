import lzma
# Test LZMADecompressor for non-consecutive reads

data = lzma.compress(b"abcd")
decompressor = lzma.LZMADecompressor()
decompressor.decompress(data[:2])
decompressor.decompress(data[2:])
# Test LZMADecompressor.decompress(eof=True) with no data left, just header

data = lzma.compress(b"abcd")
decompressor = lzma.LZMADecompressor()
decompressor.decompress(data[:-5], eof=True)
# Test LZMADecompressor.decompress(eof=True) with leftover data

data = lzma.compress(b"abcd")
decompressor = lzma.LZMADecompressor()
try:
    decompressor.decompress(data, eof=True)
except EOFError:
    pass
else:
    print("EOFError not raised")
# Test LZMADecompressor.dec
