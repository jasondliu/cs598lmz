import lzma
# Test LZMADecompressor
lzc = lzma.LZMADecompressor()
decompressed = lzc.decompress(compressed)
print(decompressed)

# Test LZMACompressor
lzc = lzma.LZMACompressor()
compressed = lzc.compress(b"Hello world!\n")
compressed += lzc.flush()
print(compressed)

# Test LZMADecompressor
lzc = lzma.LZMADecompressor()
decompressed = lzc.decompress(compressed)
print(decompressed)

print(lzc.eof)

# Test LZMADecompressor
lzc = lzma.LZMADecompressor()
decompressed = lzc.decompress(compressed)
print(decompressed)

print(lzc.eof)

# Test LZMADecompressor
lzc = lzma.LZMADecompressor()
decompressed =
