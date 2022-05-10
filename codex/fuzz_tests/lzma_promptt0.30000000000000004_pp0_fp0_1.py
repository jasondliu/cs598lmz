import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress the data
uncompressed_data = decompressor.decompress(compressed_data)

# Print the size of the uncompressed data
print('Uncompressed Data Size :', len(uncompressed_data))

# Print the first 10 bytes of the uncompressed data
print('First 10 Bytes :', uncompressed_data[:10])

# Print the last 10 bytes of the uncompressed data
print('Last 10 Bytes :', uncompressed_data[-10:])

# Print the uncompressed data
print(uncompressed_data)

# Print the compressed data
print(compressed_data)

# Print the size of the compressed data
print('Compressed Data Size :', len(compressed_data))

# Print the size of the uncompressed data
print('Uncompressed Data Size :', len(uncompressed_data))

# Print the first 10 bytes of the uncompressed data
print('First 10 Bytes :', uncompressed_data[
