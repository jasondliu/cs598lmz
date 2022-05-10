import lzma
# Test LZMADecompressor
with open("/tmp/test.xz", "rb") as f:
    decompressor = lzma.LZMADecompressor()
    data = f.read(1024)
    while data:
        print(decompressor.decompress(data))
        data = f.read(1024)
    print(decompressor.flush())

# Test LZMAFile
with lzma.open("/tmp/test.xz") as f:
    print(f.read())

# Test LZMAFile with filters
with lzma.open("/tmp/test.xz", filters=[{"id": lzma.FILTER_LZMA2, "preset": 3}]) as f:
    print(f.read())

# Test LZMAFile with mode "w"
with lzma.open("/tmp/test.xz", mode="w") as f:
    f.write(b"test")

# Test LZMAFile with mode "w" and filters
with lzma.open("/tmp/test.xz
