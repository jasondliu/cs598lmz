import lzma
# Test LZMADecompressor

# LZMA Decompressor
decompressor = lzma.LZMADecompressor()

# Read compressed data from file
with open('data/compressed_data.xz', 'rb') as f:
    data = f.read()

# Decompress data
decompressed_data = decompressor.decompress(data)

# Print decompressed data
print(decompressed_data)

# Print original data
print(decompressor.unused_data)

# Print number of unconsumed bytes
print(len(decompressor.unused_data))

# Print number of unconsumed bytes
print(decompressor.eof)

# Print number of unconsumed bytes
print(decompressor.needs_input)

# Print number of unconsumed bytes
print(decompressor.needs_input)

# Print number of unconsumed bytes
print(decompressor.needs_input)

# Print number of unconsumed bytes
print(decompressor.needs_input)

# Print number of unconsumed bytes
print(decompressor
