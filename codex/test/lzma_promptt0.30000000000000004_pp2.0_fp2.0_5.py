import lzma
# Test LZMADecompressor
#
# The following test is based on the example in PEP-3101.

# Create a compressor object
comp = lzma.LZMACompressor()

# Compress some data
data = comp.compress(b"Hello world!")
data += comp.flush()

# Create a decompressor object
decomp = lzma.LZMADecompressor()

# Decompress the data
print(decomp.decompress(data))

# Decompress the rest of the data
print(decomp.unused_data)

# Decompress the data
