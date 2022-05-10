import lzma
# Test LZMADecompressor

# The simplest way to use LZMADecompressor is to read it in a loop.
# The read() method reads more data from the decompressor.
# If the data returned is empty, the end of the compressed data has been reached.

compressor = lzma.LZMACompressor()

# Compress some data
data = b'This is the original text.'
compressed = compressor.compress(data)
# Flush the compressor to get the data that was buffered
compressed += compressor.flush()

# Create a LZMADecompressor object
decompressor = lzma.LZMADecompressor()

# Decompress the data
decompressed = decompressor.decompress(compressed)

# Check that the original data is the same as the decompressed data
assert data == decompressed

# The decompressor object can be used multiple times.
# This is useful if you want to decompress multiple compressed streams in a row.

# Compress the data again
