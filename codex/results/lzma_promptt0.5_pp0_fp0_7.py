import lzma
# Test LZMADecompressor.__init__()

# Test without arguments
decompressor = lzma.LZMADecompressor()

# Test with arguments
decompressor = lzma.LZMADecompressor(format=lzma.FORMAT_XZ, filters=[{"id": lzma.FILTER_LZMA2, "preset": 3}])

# Test with invalid arguments
try:
    decompressor = lzma.LZMADecompressor(format=42)
except ValueError:
    print("ValueError")

try:
    decompressor = lzma.LZMADecompressor(filters=[42])
except ValueError:
    print("ValueError")

try:
    decompressor = lzma.LZMADecompressor(filters=[{"id": 42}])
except ValueError:
    print("ValueError")

try:
    decompressor = lzma.LZMADecompressor(filters=[{"id": lzma.FILTER_LZMA2, "preset": 42}])
