import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress the data
decompressed_data = decompressor.decompress(compressed_data)

# Print the size of the decompressed data
print('Decompressed Data : {}'.format(len(decompressed_data)))

# Print the decompressed data itself
print(decompressed_data)

# Print the original data
print('Original Data : {}'.format(len(original_data)))
print(original_data)

# Print a sample of original and decompressed data
print('Sample of Original Data : {}'.format(original_data[:10]))
print('Sample of Decompressed Data : {}'.format(decompressed_data[:10]))

# Print the end of original and decompressed data
print('Sample of Original Data : {}'.format(original_data[-10:]))
print('Sample of Decompressed Data : {}'.format(decompressed_data[-10:]))

# Print the status of the decompressor object
print
