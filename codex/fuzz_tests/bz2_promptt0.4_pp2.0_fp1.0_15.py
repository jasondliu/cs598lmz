import bz2
# Test BZ2Decompressor

# Create decompressor object
decompressor = bz2.BZ2Decompressor()

# Decompress data
uncompressed_data = decompressor.decompress(compressed_data)

# Print the result
print('Decompressed is {} bytes'.format(len(uncompressed_data)))
print(uncompressed_data)

# Decompress more data
more_data = decompressor.decompress(compressed_data)

# Print the result
print('Decompressed is {} bytes'.format(len(more_data)))
print(more_data)

# Decompress more data
more_data = decompressor.decompress(compressed_data)

# Print the result
print('Decompressed is {} bytes'.format(len(more_data)))
print(more_data)

# Decompress more data
more_data = decompressor.decompress(compressed_data)

# Print the result
print('Decompressed is {} bytes'.format(len(more_data)))
print(more_data)

# Dec
