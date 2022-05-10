import lzma
# Test LZMADecompressor

# Create a compressor object
comp = lzma.LZMACompressor()

# Compress some data
data = comp.compress(b"Hello world!")
print(data)

# Finish the compression process
data += comp.flush()
print(data)

# Create a decompressor object
decomp = lzma.LZMADecompressor()

# Decompress the data
print(decomp.decompress(data))

# Decompress the data
