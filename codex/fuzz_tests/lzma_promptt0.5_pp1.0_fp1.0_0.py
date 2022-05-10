import lzma
# Test LZMADecompressor

# Test for basic operation

data = b'\x00' * 5 + lzma.compress(b'a' * 10)
decomp = lzma.LZMADecompressor()
result = decomp.decompress(data)
assert result == b'a' * 10

# Test for multiple calls to decompress()

data = lzma.compress(b'a' * 10)
decomp = lzma.LZMADecompressor()
result = decomp.decompress(data[:5])
result += decomp.decompress(data[5:])
assert result == b'a' * 10

# Test for multiple calls to decompress() with unconsumed data

data = lzma.compress(b'a' * 10)
decomp = lzma.LZMADecompressor()
result = decomp.decompress(data[:5])
result += decomp.decompress(data[5:-5])
result += decomp.decompress(data[-5:])
assert result == b'a' *
