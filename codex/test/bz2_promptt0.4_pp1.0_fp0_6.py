import bz2
# Test BZ2Decompressor

# Test BZ2Decompressor.flush()

data = bz2.compress(b"this is a test")
decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data))
