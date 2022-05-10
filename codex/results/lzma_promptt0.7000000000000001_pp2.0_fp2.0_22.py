import lzma
# Test LZMADecompressor().decompress() method
x = b"1234" * 1000000
lzc = lzma.LZMACompressor()
y = lzc.compress(x)
y += lzc.flush()
lzd = lzma.LZMADecompressor()
x2 = lzd.decompress(y)
x2 += lzd.decompress(b"\x00\x00\x00\x00")
assert x == x2
# Test LZMADecompressor().flush() method
x = b"1234" * 1000000
lzc = lzma.LZMACompressor()
y = lzc.compress(x)
y += lzc.flush()
lzd = lzma.LZMADecompressor()
x2 = lzd.decompress(y)
assert x == x2
# Test LZMADecompressor().decompress() method with multiple chunks
x = b"1234" * 1000000
lzc = lzma.LZ
