import lzma
# Test LZMADecompressor

# Create a decompressor
decompressor = lzma.LZMADecompressor()

# Read the compressed data
with open('data/python.xz', 'rb') as f:
    compressed_data = f.read()

# Decompress the compressed data
data = decompressor.decompress(compressed_data)

# Display the decompressed data
print(data)

# Close the decompressor
decompressor.flush()

# Display the decompressor's unused data
print(decompressor.unused_data)

# Close the decompressor
decompressor.close()

# Display the decompressor's unused data
print(decompressor.unused_data)

# Read the compressed data
with open('data/python.xz', 'rb') as f:
    compressed_data = f.read()

# Decompress the compressed data
data = decompressor.decompress(compressed_data)

# Display the decompressed data
print(data)

# Close the decompressor
decompressor.flush()

# Display
