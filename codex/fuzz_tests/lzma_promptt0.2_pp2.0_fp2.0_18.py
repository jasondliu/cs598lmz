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
print('Decompressed: {} bytes'.format(len(decompressed_data)))

# Print the decompressed data, converting each byte to a character
print(decompressed_data.decode('utf-8'))

# Compress the data
compressed_data = lzma.compress(data)

# Print the size of the compressed data
print('Compressed: {} bytes'.format(len(compressed_data)))

# Decompress the data
decompressed_data = lzma.decompress(compressed_data)

# Print the size of the decompressed data
print('Decompressed
