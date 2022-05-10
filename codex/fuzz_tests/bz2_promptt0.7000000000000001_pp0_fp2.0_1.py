import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
uncompressed_data = decompressor.decompress(compressed_data)
uncompressed_data

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
compressor.compress(uncompressed_data)
compressor.flush()
# Compare the original data to the decompressed data
data == uncompressed_data

# Compress the data again
compressed_data = bz2.compress(data)
# Decompress again
uncompressed_data = bz2.decompress(compressed_data)
# Verify that it matches the original data
data == uncompressed_data

# Read compressed file
file_data = bz2.BZ2File('./compressed_data.bz2', 'rb')

# Decompress the data
uncompressed_data = file_data.read()

# Verify that it matches the original data
data == uncompressed_data

# Write compressed file
file_data = bz2.BZ2
