import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

# Read the first 5 bytes of the compressed file
with open('example.bz2', 'rb') as input:
    next_5_bytes = input.read(5)

# Decompress the first 5 bytes
decompressed_data = decompressor.decompress(next_5_bytes)

# Print the first 5 bytes of the decompressed file
print(decompressed_data)

# Print the entire decompressed file
