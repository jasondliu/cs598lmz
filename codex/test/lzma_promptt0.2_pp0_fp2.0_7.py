import lzma
# Test LZMADecompressor

# Test LZMADecompressor.__init__()

# Test LZMADecompressor.__init__() with no arguments
decompressor = lzma.LZMADecompressor()

# Test LZMADecompressor.__init__() with valid arguments
decompressor = lzma.LZMADecompressor(format=lzma.FORMAT_XZ)

# Test LZMADecompressor.__init__() with invalid arguments
try:
    decompressor = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)
except ValueError:
    pass
else:
    print("Expected ValueError")

try:
    decompressor = lzma.LZMADecompressor(format=lzma.FORMAT_RAW)
except ValueError:
    pass
else:
    print("Expected ValueError")

