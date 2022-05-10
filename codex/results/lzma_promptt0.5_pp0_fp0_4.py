import lzma
# Test LZMADecompressor
d = lzma.LZMADecompressor()
result = d.decompress(compressed_data)
print(result)

# Test LZMACompressor
c = lzma.LZMACompressor()
result = c.compress(data)
print(result)

# Test LZMADecompressor with multiple chunks
d = lzma.LZMADecompressor()
result = d.decompress(compressed_data)
result += d.decompress(compressed_data)
print(result)

# Test LZMACompressor with multiple chunks
c = lzma.LZMACompressor()
result = c.compress(data)
result += c.compress(data)
print(result)

# Test LZMADecompressor with multiple chunks and a filler
d = lzma.LZMADecompressor()
result = d.decompress(compressed_data)
result += d.decompress(compressed_data)
result += d.decompress(b'\x
