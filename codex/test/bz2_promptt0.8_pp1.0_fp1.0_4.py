import bz2
# Test BZ2Decompressor with a string
data = bz2.compress(b"testing")
decompressor = bz2.BZ2Decompressor()
orig = decompressor.decompress(data)
print(orig)

# Test BZ2Decompressor with a file
