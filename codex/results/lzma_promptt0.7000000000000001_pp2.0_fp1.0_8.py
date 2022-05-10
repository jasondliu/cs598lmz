import lzma
# Test LZMADecompressor

# Create a data set for compression
data = os.urandom(1048576)

# Compress
cdata = lzma.compress(data)

# Decompressor
decompressor = lzma.LZMADecompressor()

# Decompress to the same size
d1 = decompressor.decompress(cdata)
assert len(d1) == len(data)

# Decompress partially to half the size
d2 = decompressor.decompress(cdata, max_length=len(data)//2)
assert len(d2) == len(data)//2

# Decompress the rest
d3 = decompressor.decompress(cdata, max_length=len(data)//2)
assert len(d3) == len(data)//2

# Now get the complete data
d4 = d2 + d3

# Compare the decompressed data
assert d4 == data

# Test the LZMADecompressor with a stream

# Decompressor
decompressor = lzma.
