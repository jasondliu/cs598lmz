import bz2
# Test BZ2Decompressor

compressed = bz2.BZ2Compressor().compress(b"this is a test")
print(compressed)

decompressed = bz2.BZ2Decompressor().decompress(compressed)
print(decompressed)

# Test BZ2File

with open("/tmp/bz2_file.bz2", "wb") as file:
    file.write(compressed)

with bz2.BZ2File("/tmp/bz2_file.bz2", "r") as file:
    data = file.read()
    print(data)
