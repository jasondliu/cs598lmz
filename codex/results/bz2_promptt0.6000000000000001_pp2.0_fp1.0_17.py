import bz2
# Test BZ2Decompressor Object
bz2_decompressor = bz2.BZ2Decompressor()

# Decompress the compressed file
uncompressed_data = bz2_decompressor.decompress(compressed_data)

# Print the uncompressed data
print("Decompressed:",uncompressed_data)

# Print the original data
print("Original:",data)

# Verify that you have the original data
print("The two are equal:",uncompressed_data == data)

# Create a BZ2File Object
bz2_file = bz2.BZ2File('example.bz2', 'wb')

# Write the compressed data to the file
bz2_file.write(compressed_data)

# Flush the data to the file
bz2_file.flush()

# Close the file
bz2_file.close()

# Create a BZ2File Object
bz2_file = bz2.BZ2File('example.bz2', 'rb')

# Print the decompressed data
print
