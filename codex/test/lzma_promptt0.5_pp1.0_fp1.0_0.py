import lzma
# Test LZMADecompressor

# Test for basic operation

data = b'\x00' * 5 + lzma.compress(b'a' * 10)
decomp = lzma.LZMADecompressor()
