import bz2
# Test BZ2Decompressor

# Create a decompressor object
decompressor = bz2.BZ2Decompressor()

# Decompress the data
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

# Print the first 100 characters of the uncompressed data
print(uncompressed_data[:100])
 
# Print the first 100 characters of the original data
print(original_data[:100])
 
# Print the first 100 characters of the compressed data
print(compressed_data[:100])
 
# Print the first 100 characters of the compressed data
print(compressed_data[:100])

# Print the first 100 characters of the uncompressed data
print
