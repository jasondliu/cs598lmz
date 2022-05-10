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
decompressor.decompress(compressed1)
decompressor.decompress(compressed2)
print(decompressor.decompress(compressed))

try:
    print(decompressor.decompress(compressed1))
except ValueError:
    pass

try:
    print(decompressor.decompress(compressed1, max_length=2))
except ValueError:
    pass
try:
    print(decompressor.decompress(comp
