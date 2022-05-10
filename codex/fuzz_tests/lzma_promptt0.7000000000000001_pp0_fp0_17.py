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

for chunk in [compressed[:1000], compressed[1000:2000], compressed[2000:]]:
    result += decompressor.decompress(chunk)

assert result == data
print("OK")

# Test LZMADecompressor.unused_data.

decompressor = lzma.LZMADecompressor()
decompressor.decompress(compressed)

assert decompressor.unused_data == b""
print("OK")

# Test EOF handling.

decompressor = lzma.LZMADecompressor()
decompressor.decompress(compressed
