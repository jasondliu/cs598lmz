import lzma
# Test LZMADecompressor

with open("test.xz", "rb") as f:
    d = lzma.LZMADecompressor()
    out = d.decompress(f.read())
    print(out)

# Test LZMACompressor

c = lzma.LZMACompressor()
with open("test.xz", "wb") as f:
    f.write(c.compress(b"Hello World!"))
    f.write(c.flush())

with open("test.xz", "rb") as f:
    d = lzma.LZMADecompressor()
    out = d.decompress(f.read())
    print(out)

# Test LZMADecompressor.decompress()

with open("test.xz", "rb") as f:
    d = lzma.LZMADecompressor()
    out = d.decompress(f.read())
    print(out)

# Test LZMADecompressor.decompress()

