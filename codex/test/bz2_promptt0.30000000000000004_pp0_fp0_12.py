import bz2
# Test BZ2Decompressor

# Create a BZ2Decompressor object
decompressor = bz2.BZ2Decompressor()

# Decompress the first 3 bytes
print(decompressor.decompress(b'BZh'))

# Read one byte, decompress and print it
