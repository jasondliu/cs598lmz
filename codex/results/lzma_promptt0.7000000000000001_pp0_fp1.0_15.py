import lzma
# Test LZMADecompressor
decomp = lzma.LZMADecompressor()

with open('../data/path/to/lzma/file', 'rb') as f:
    compressed_data = f.read()

# Decompress the file using the LZMADecompressor object
decompressed_data = decomp.decompress(compressed_data)

# Print a preview of the decompressed data
print(decompressed_data[:100])
"""
b'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc quis diam mi. Sed le'
"""
# Close the decompressor object
decomp.flush()

# Print the length of the decompressed data
print(len(decompressed_data))
"""
2318
"""
 
# Compress a file using XZ compression
import lzma

with open('../data/path/to/uncompressed_file', 'rb') as f_in:
    with lzma.open('../data/path/to/lzma_file', 'w
