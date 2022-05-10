import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()

# Decompress the data
decompressed_data = decompressor.decompress(compressed_data)

# Print the length of the decompressed data
print('Decompressed Length: {}'.format(len(decompressed_data)))

# Print the first 1000 characters of the decompressed data
print(decompressed_data[:1000])

# Test BZ2Decompressor with max_length
decompressor = bz2.BZ2Decompressor()

# Decompress the first 5 bytes
uncompressed_data = decompressor.decompress(compressed_data, max_length=5)

# Print the result
print(uncompressed_data)

# Test BZ2Decompressor with max_length
decompressor = bz2.BZ2Decompressor()

# Decompress the first 5 bytes
uncompressed_data = decompressor.decompress(compressed_data, max_length=5)

# Decompress the rest of the data

