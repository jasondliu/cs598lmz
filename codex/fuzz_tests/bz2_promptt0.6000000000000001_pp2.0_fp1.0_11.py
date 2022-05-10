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
data = d.decompress(b"This is another test")
print(data)

# There is no more data left
try:
    data = d.decompress(b"")
except EOFError:
    print("Caught EOF error")

# Test that the BZ2Compressor object can be reused
data = c.compress(b"This is another test")
print(data)

data =
