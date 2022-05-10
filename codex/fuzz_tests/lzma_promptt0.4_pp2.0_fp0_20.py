import lzma
# Test LZMADecompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Compress some data
data = b"Hello world!"
compressed = compressor.compress(data)

# Finish compression
compressed += compressor.flush()

# Decompress with an empty decompressor object
decompressed = decompressor.decompress(compressed)

# Decompress with a decompressor object that has some history
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)

# Decompress with a decompressor object that has some history and
# some unused data
decompressor = lzma.LZMADecompressor()
decompressor.decompress(compressed[:-5])
decompressed = decompressor.decompress(compressed[-5:])

# Decompress with a decompressor object that has some history and
# some unused data, but the unused
