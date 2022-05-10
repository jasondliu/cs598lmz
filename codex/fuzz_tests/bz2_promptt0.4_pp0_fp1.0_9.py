import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# Decompress the entire file with bz2.decompress()
uncompressed_data = bz2.decompress(compressed_data)

# Write the decompressed file
with open('uncompressed_file.txt', 'wb') as f:
    f.write(uncompressed_data)

# Read the original and decompressed file contents
with open('uncompressed_file.txt', 'rb') as f:
    print(f.read())

# Compress a file with bz2.compress()
with open('uncompressed_file.txt', 'rb') as f:
    compressed_data = bz2.compress(f.read())

# Write the compressed file
with open('compressed_file.bz2', 'wb') as f:
    f.write(compressed_data)

# Read the compressed and decompressed file contents
with open('compressed_file.bz2', 'rb
