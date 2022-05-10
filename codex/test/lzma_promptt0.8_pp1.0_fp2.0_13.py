import lzma
# Test LZMADecompressor
lzc = lzma.LZMADecompressor()
ret = lzc.decompress(b"\x00")
print(ret)

# Test LZMADecompressor.decompress(data, max_length)
# This should throw a MemoryError
lzc = lzma.LZMADecompressor()
ret = lzc.decompress(b"\x00", 0)
