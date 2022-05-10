import lzma
# Test LZMADecompressor().decompress() method
x = b"1234" * 1000000
lzc = lzma.LZMACompressor()
y = lzc.compress(x)
y += lzc.flush()
lzd = lzma.LZMADecompressor()
x2 = lzd.decompress(y)
