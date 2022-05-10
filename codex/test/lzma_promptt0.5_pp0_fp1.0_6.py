import lzma
# Test LZMADecompressor

with open("test.xz", "rb") as f:
    decompressor = lzma.LZMADecompressor()
    data = f.read(100)
    print(decompressor.decompress(data))
    data = f.read()
