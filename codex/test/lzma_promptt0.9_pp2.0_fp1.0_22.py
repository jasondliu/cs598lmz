import lzma
# Test LZMADecompressor Class
data = b"X" * 100 + lzma.compress(b"Y" * 100)
