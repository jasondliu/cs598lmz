import lzma
# Test LZMADecompressor
s = b"x" * 100 + lzma.compress(b"hello world")
c = lzma.LZMADecompressor()
