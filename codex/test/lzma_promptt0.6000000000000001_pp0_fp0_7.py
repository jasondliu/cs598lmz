import lzma
# Test LZMADecompressor

compressed = lzma.compress(b"test")
print(compressed)

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
print(decompressed)

print(decompressor.eof)

# Test LZMAFile

with open("test.xz", "wb") as f:
    f.write(lzma.compress(b"test"))

with lzma.open("test.xz") as f:
    print(f.read())

print(f.closed)

# Test LZMAError

