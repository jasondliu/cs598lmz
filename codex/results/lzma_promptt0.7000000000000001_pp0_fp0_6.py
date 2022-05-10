import lzma
# Test LZMADecompressor.decompress()
# https://docs.python.org/3.6/library/lzma.html#lzma.LZMADecompressor.decompress

# Create a Compressor object
decompressor = lzma.LZMADecompressor()

# Decompress the data
decompressed_data = decompressor.decompress(compressed_data)

# Make sure the decompression worked
if decompressed_data == original_data:
    print('Success!')
else:
    print('Failure!')

# Print out the decompressed data
print(decompressed_data)

# Print out how many bytes the decompressed data has
print(f'Length of decompressed data: {len(decompressed_data)}')

# Print out how many bytes the original data has
print(f'Length of original data: {len(original_data)}')



# Code from: https://stackoverflow.com/questions/27631382/python-lzma-decompression-of-string-returns-incorrect-
