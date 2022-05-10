import bz2
# Test BZ2Decompressor

# Create a compressor object
decompressor = bz2.BZ2Decompressor()

# Decompress the data
decompressed_data = decompressor.decompress(compressed_data)

# The decompressed data is a bytes object
print(type(decompressed_data))

# Print the first 100 bytes of the decompressed data
print(decompressed_data[:100])

# Decompress the data
decompressed_data = bz2.decompress(compressed_data)

# Print the first 100 bytes of the decompressed data
print(decompressed_data[:100])

# Decompress the data
decompressed_data = bz2.decompress(compressed_data)

# The decompressed data is a bytes object
print(type(decompressed_data))

# Print the first 100 bytes of the decompressed data
print(decompressed_data[:100])
 
# Decompress the data
decompressed_data = bz2.decompress(compressed_data)


