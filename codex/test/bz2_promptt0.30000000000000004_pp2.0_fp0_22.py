import bz2
# Test BZ2Decompressor

# Create a decompressor object
decompressor = bz2.BZ2Decompressor()

# Decompress the first 3 characters
print(decompressor.decompress(b'BZh'))

# Decompress the next 5 characters
