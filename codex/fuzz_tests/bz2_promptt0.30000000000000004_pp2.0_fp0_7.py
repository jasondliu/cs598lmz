import bz2
# Test BZ2Decompressor

# Create a decompressor object
decompressor = bz2.BZ2Decompressor()

# Decompress the compressed data
uncompressed_data = decompressor.decompress(compressed_data)

# Print the uncompressed data
print(uncompressed_data)

# Print the original data
print(original_data)

# Print the length of the original data
print(len(original_data))

# Print the length of the compressed data
print(len(compressed_data))

# Print the length of the uncompressed data
print(len(uncompressed_data))
 
# Compress the data using BZ2
compressed_data = bz2.compress(original_data)

# Decompress the data using BZ2
uncompressed_data = bz2.decompress(compressed_data)

# Print the uncompressed data
print(uncompressed_data)

# Print the original data
print(original_data)

# Print the length of the original data
print(len(original_data))

