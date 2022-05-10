import lzma
# Test LZMADecompressor
x = b"a"*100000
compressed = lzma.compress(x)
compressor = lzma.LZMACompressor()
compressed1 = compressor.compress(x)
compressed2 = compressor.compress(x)
compressed += compressor.flush()
print(len(compressed))
print(len(compressed1))
print(len(compressed2))
decompressor = lzma.LZMADecompressor()
try:
    print(decompressor.decompress(compressed))
except ValueError:
    pass
