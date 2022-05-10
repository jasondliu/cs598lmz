import bz2
# Test BZ2Decompressor

data = bz2.compress(bytes(range(256)))

# Create a decoder object
decompressor = bz2.BZ2Decompressor()

# Decompress the data
decompressor.decompress(data)

# Decompress the data, and return the chunk size
