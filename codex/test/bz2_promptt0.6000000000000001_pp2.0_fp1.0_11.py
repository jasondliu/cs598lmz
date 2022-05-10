import bz2
# Test BZ2Decompressor

# Create a BZ2Compressor object
c = bz2.BZ2Compressor()

# Create a BZ2Decompressor object
d = bz2.BZ2Decompressor()

# Compress a piece of data
data = c.compress(b"This is a test")
print(data)

# Decompress the data
data = d.decompress(data)
print(data)

# Flush remaining data
data = c.flush()
print(data)

data = d.decompress(data)
print(data)

# Test that the BZ2Decompressor object can be reused
