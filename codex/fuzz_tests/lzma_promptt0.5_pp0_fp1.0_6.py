import lzma
# Test LZMADecompressor

with open("test.xz", "rb") as f:
    decompressor = lzma.LZMADecompressor()
    data = f.read(100)
    print(decompressor.decompress(data))
    data = f.read()
    print(decompressor.decompress(data))

# Test LZMADecompressor.decompress()

with open("test.xz", "rb") as f:
    decompressor = lzma.LZMADecompressor()
    print(decompressor.decompress(f.read()))

# Test LZMADecompressor.decompress() with max_length

with open("test.xz", "rb") as f:
    decompressor = lzma.LZMADecompressor()
    print(decompressor.decompress(f.read(), max_length=2))
    print(decompressor.decompress(f.read(), max_length=2))
    print(decompressor.decompress(f.
