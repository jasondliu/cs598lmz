import lzma
# Test LZMADecompressor.__init__(), and LZMADecompressor.__call__()

# Create an LZMA object to decompress data incrementally.
d = lzma.LZMADecompressor()

# Feed data in chunks, and collect the results.
data = []
