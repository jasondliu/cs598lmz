import lzma
# Test LZMADecompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Compress some data
data = b'Lots of data, lots of data, lots of data, lots of data, lots of data'
compressed = compressor.compress(data)
compressed += compressor.flush()

# Decompress the data
decompressed = decompressor.decompress(compressed)
print(decompressed)

# The final decompressed data is still in the buffer
# so we can decompress more data into the same buffer
