import lzma
# Test LZMADecompressor with a file-like object

data = b"x" * 100000 + lzma.compress(b"foo") + b"x" * 100000

with open("foo.xz", "wb") as f:
    f.write(data)

with open("foo.xz", "rb") as f:
    decompressor = lzma.LZMADecompressor()
