import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress the data
decompressed_data = decompressor.decompress(compressed_data)

# Decompress the data
decompressed_data = decompressor.decompress(compressed_data)

# Finish the decompression
decompressed_data += decompressor.flush()

# Print the size of the decompressed data
print('Decompressed is {} bytes'.format(len(decompressed_data)))

# Print the decompressed data
print(decompressed_data)

# Print the first 30 characters of the decompressed data
print(decompressed_data[:30])
 
# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress the data
decompressed_data = decompressor.decompress(compressed_data)

# Finish the decompression
decompressed_data += decompressor.flush()

# Print the size of the decompressed data
print
