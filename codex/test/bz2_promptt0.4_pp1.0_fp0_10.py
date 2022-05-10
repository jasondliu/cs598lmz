import bz2
# Test BZ2Decompressor.decompress()

# Decompress a small string
decompressor = bz2.BZ2Decompressor()
s = decompressor.decompress(bz2.compress(b"this is a test"))
print(s)

# Decompress a file
