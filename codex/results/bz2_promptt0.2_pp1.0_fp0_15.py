import bz2
# Test BZ2Decompressor

# Create a decompressor object
decompressor = bz2.BZ2Decompressor()

# Decompress the compressed data
uncompressed_data = decompressor.decompress(compressed_data)

# Print the size of the uncompressed data
print('The uncompressed data is {} bytes'.format(len(uncompressed_data)))

# Print the first 100 characters in the uncompressed data
print(uncompressed_data[:100])

# Import the BZ2File class
from bz2 import BZ2File

# Create a BZ2File object
bz2_file = BZ2File('example.bz2')

# Read the compressed data
file_content = bz2_file.read()

# Print the size of the compressed data
print('The size of the compressed file is {} bytes'.format(len(file_content)))

# Print the first 100 characters in the compressed data
print(file_content[:100])

# Import the BZ2File class
from bz2 import BZ2File

# Create a B
