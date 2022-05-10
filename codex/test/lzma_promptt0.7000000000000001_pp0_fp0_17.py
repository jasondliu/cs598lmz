import lzma
# Test LZMADecompressor.

data = b"1234567890" * 1000000
compressed = lzma.compress(data)

decompressor = lzma.LZMADecompressor()
result = decompressor.decompress(compressed)

assert result == data
print("OK")

# Test LZMADecompressor object.

decompressor = lzma.LZMADecompressor()
result = b""

