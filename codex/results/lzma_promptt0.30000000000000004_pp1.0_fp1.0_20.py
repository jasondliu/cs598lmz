import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to kick things off
next_byte = f.read(1)

# Keep going until there's no more input
while next_byte:
    # Feed the decompressor object with the next byte
    decompressor.decompress(next_byte)
    
    # Read the next byte
    next_byte = f.read(1)

# Finish decompression
decompressed_data = decompressor.flush()

# Show the decompressed data
print(decompressed_data)

# Close the file
f.close()
 
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, just to kick things off
next_byte = f.read(1)

# Keep going until there's no more input
while next_byte:
    # Feed the decompressor object with the next byte
    decompressor.decompress(next
