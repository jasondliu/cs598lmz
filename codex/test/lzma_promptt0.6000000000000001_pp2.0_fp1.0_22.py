import lzma
# Test LZMADecompressor

data = b"X" * 100 + lzma.compress(b"test") + b"Y" * 100

decomp = lzma.LZMADecompressor()

