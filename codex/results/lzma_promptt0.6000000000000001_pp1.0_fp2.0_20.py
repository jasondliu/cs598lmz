import lzma
# Test LZMADecompressor()
with open("file.xz", "rb") as f:
    decompressor = lzma.LZMADecompressor()
    with open("file", "wb") as g:
        for data in iter(lambda: f.read(1024 * 1024), b""):
            g.write(decompressor.decompress(data))
        g.write(decompressor.flush())
# Test LZMAFile()
with lzma.LZMAFile("file.xz") as f:
    with open("file", "wb") as g:
        while True:
            data = f.read(1024 * 1024)
            if not data:
                break
            g.write(data)
</code>

