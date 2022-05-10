import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress the data
decompressed_data = decompressor.decompress(compressed_data)

# Print the size of the uncompressed data
print("Size of the uncompressed data: {}".format(len(decompressed_data)))

# Print the decompressed data
print(decompressed_data)

# Print the original data
print(data)

# Compress the data
compressed_data = lzma.compress(data)

# Print the size of the compressed data
print("Size of the compressed data: {}".format(len(compressed_data)))

# Decompress the data
decompressed_data = lzma.decompress(compressed_data)

# Print the size of the decompressed data
print("Size of the decompressed data: {}".format(len(decompressed_data)))

# Print the original data
print(decompressed_data)

# Print the original data
print(data)

