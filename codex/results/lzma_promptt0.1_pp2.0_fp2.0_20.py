import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress the data
decompressed_data = decompressor.decompress(compressed_data)

# Finish the decompression process
decompressed_data += decompressor.flush()

# Print the size of the decompressed data
print('Decompressed Size:', len(decompressed_data))

# Print the decompressed data itself
print(decompressed_data)

# Print the original data
print(original_data)

# Print a success message
print('All OK')

# Compress the data
compressed_data = lzma.compress(original_data)

# Print the size of the compressed data
print('Compressed Size:', len(compressed_data))

# Decompress the data
decompressed_data = lzma.decompress(compressed_data)

# Print the size of the decompressed data
print('Decompressed Size:', len(decompressed_data))

# Print the original
