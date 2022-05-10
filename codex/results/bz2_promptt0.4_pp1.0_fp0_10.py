import bz2
# Test BZ2Decompressor.decompress()

# Decompress a small string
decompressor = bz2.BZ2Decompressor()
s = decompressor.decompress(bz2.compress(b"this is a test"))
print(s)

# Decompress a file
with bz2.open("testfile.bz2", "rb") as source:
    with open("testfile.out", "wb") as dest:
        decompressor = bz2.BZ2Decompressor()
        for data in iter(lambda: source.read(100 * 1024), b""):
            dest.write(decompressor.decompress(data))

# Decompress a file in chunks
with bz2.open("testfile.bz2", "rb") as source:
    with open("testfile.out", "wb") as dest:
        decompressor = bz2.BZ2Decompressor()
        for data in iter(lambda: source.read(100 * 1024), b""):
            dest.write(decompressor.decompress(data))

