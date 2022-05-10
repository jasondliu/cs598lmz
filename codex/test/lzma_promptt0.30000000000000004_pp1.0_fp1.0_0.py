import lzma
# Test LZMADecompressor

# Create a compressor object
c = lzma.LZMADecompressor()

# Compress some data
data = b"Hello world! " * 1000
