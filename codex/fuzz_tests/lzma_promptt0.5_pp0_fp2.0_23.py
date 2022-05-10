import lzma
# Test LZMADecompressor
with open("lzma_file", "rb") as f:
    decompressor = lzma.LZMADecompressor()
    data = f.read(1024)
    while data:
        print(decompressor.decompress(data))
        data = f.read(1024)

# Test LZMACompressor
with open("lzma_file", "wb") as f:
    compressor = lzma.LZMACompressor()
    f.write(compressor.compress(b"Hello world"))
    f.write(compressor.flush())

# Test open
with lzma.open("lzma_file", "rt") as f:
    print(f.read())

with lzma.open("lzma_file", "wt") as f:
    f.write("Hello world")

# Test decompress
with open("lzma_file", "rb") as f:
    print(lzma.decompress(f.read()))

# Test compress
with open("lzma_file",
