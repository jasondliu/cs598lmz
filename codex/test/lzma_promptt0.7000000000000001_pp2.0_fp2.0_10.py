import lzma
# Test LZMADecompressor in streaming mode

# Source data contains a short string of ASCII text
data = b"This is a test. This is only a test."

# Create a LZMADecompressor object
decompressor = lzma.LZMADecompressor()

# Decompress data in chunks, returning uncompressed data as chunks
