from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# Compress bz2_data
bz2_comp = BZ2Compressor()
result = bz2_comp.compress(bz2_data)
result += bz2_comp.flush()
len(result)

# Decompress from file
with open('bz2_compressed.txt', 'rb') as f:
    file_content = f.read()

# Build a BZ2Decompressor object
decompressor = BZ2Decompressor()

# Decompress the file content
decompressed_data = decompressor.decompress(file_content)

# Write the decompressed data to a file
with open('uncompressed.txt', 'wb') as f:
    f.write(decompressed_data)

# Compress the data
bz2_comp = BZ2Compressor()
result = bz2_comp.compress(bz2_data)
result += bz2_comp.flush()

# Print the number of bytes of compressed data

