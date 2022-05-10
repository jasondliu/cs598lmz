import lzma
# Test LZMADecompressor()
with open("file.xz", "rb") as f:
    decompressor = lzma.LZMADecompressor()
    with open("file", "wb") as g:
        for data in iter(lambda: f.read(1024 * 1024), b""):
            g.write(decompressor.decompress(data))
