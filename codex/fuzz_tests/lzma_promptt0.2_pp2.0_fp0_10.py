import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to kick things off
next_byte = decompressor.decompress(b'x\x9c')

# Read all remaining data
data = decompressor.decompress()

# Finish the decompression process
data += decompressor.flush()

# Print the result
print(data)

# Clean up
del decompressor

# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to kick things off
next_byte = decompressor.decompress(b'x\x9c')

# Read all remaining data
data = decompressor.decompress()

# Finish the decompression process
data += decompressor.flush()

# Print the result
print(data)

# Clean up
del decompressor
 
# Test LZMADecompressor

# Create a decompressor object
decompressor =
