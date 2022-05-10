import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress the data
decompressed_data = decompressor.decompress(compressed_data)

# Print the length of the uncompressed data
print('Decompressed Length:', len(decompressed_data))

# Print the first 100 bytes of the uncompressed data
print(decompressed_data[:100])

# Print the last 100 bytes of the uncompressed data
print(decompressed_data[-100:])

# Print the first 100 bytes of the compressed data
print(compressed_data[:100])

# Print the last 100 bytes of the compressed data
print(compressed_data[-100:])

# Print the first 100 bytes of the compressed data
print(compressed_data[:100])

# Print the last 100 bytes of the compressed data
print(compressed_data[-100:])

# Print the first 100 bytes of the compressed data
print(compressed_data[:100])

# Print the last 100 bytes
