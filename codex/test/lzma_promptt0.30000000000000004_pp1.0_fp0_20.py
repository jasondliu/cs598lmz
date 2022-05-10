import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to kick things off
decompressor.decompress(b"\x00")

# Read all remaining data from the file
