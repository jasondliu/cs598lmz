import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()

# Decompress data
decompressed_data = decompressor.decompress(compressed_data)

# Print the length of the uncompressed data
print('Length of uncompressed data:', len(decompressed_data))

# Write the uncompressed data to a file
with open('uncompressed_file.txt', 'wb') as f:
    f.write(decompressed_data)
