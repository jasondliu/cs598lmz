import lzma
# Test LZMADecompressor

# Compress a string
compressed = lzma.compress(b'hello world')

# Decompress the compressed string
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)

# Print the decompressed string
print(decompressed)

# Print the decompressor's unused_data attribute
print(decompressor.unused_data)

# Print the decompressor's eof attribute
print(decompressor.eof)

# Print the decompressor's needs_input attribute
print(decompressor.needs_input)

# Print the decompressor's needs_input attribute
print(decompressor.needs_input)

# Decompress the compressed string again
decompressed = decompressor.decompress(compressed)

# Print the decompressed string
print(decompressed)

# Print the decompressor's unused_data attribute
print(decompressor.unused_data)

# Print the decompressor's eof attribute
print(decompressor.eof)

