import lzma
# Test LZMADecompressor
lzc = lzma.LZMADecompressor()
result = lzc.decompress(data)

# Test LZMADecompressor.decompress with max_length
lzc = lzma.LZMADecompressor()
result = lzc.decompress(data, max_length=1024)

# Test LZMADecompressor.flush()
lzc = lzma.LZMADecompressor()
result = lzc.decompress(data)
result += lzc.flush()

# Test LZMADecompressor.decompress() with max_length
lzc = lzma.LZMADecompressor()
result = b""
while True:
    chunk = lzc.decompress(data, max_length=1024)
    if not chunk:
        break
    result += chunk

# Test LZMADecompressor.multi_decompress()
lzc = lzma.LZMADecompressor()
result =
