import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress the data
decompressed_data = decompressor.decompress(compressed_data)

# Verify that the original data matches the decompressed data
print(decompressed_data == original_data)

# Print the original and decompressed data
print(original_data)
print(decompressed_data)

# Print the number of bytes of the original and decompressed data
print(len(original_data))
print(len(decompressed_data))
 
# Print the number of bytes of the compressed data
print(len(compressed_data))
 
# Print the compression ratio
print(len(compressed_data) / len(original_data))
 
# Print the decompression ratio
print(len(decompressed_data) / len(compressed_data))
 
# Print the compression and decompression ratio
print(len(original_data) / len(decompressed_data))
 
# Print the compression and decompression ratio

