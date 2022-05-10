import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress the data
decompressed_data = decompressor.decompress(compressed_data)

# Finish the decompression process
decompressed_data += decompressor.flush()

# Print the length of the decompressed data
print('Decompressed length:', len(decompressed_data))

# Verify that the data is now back to its original form
print(decompressed_data == data)

# Compress the data
compressed_data = lzma.compress(data)

# Print the length of the compressed data
print('Compressed length:', len(compressed_data))

# Decompress the compressed data
decompressed_data = lzma.decompress(compressed_data)

# Print the length of the decompressed data
print('Decompressed length:', len(decompressed_data))

# Verify that the data is now back to its original form
print(decompressed_data == data)


