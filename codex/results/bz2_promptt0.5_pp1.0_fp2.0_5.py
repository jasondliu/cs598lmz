import bz2
# Test BZ2Decompressor
from pprint import pprint

from io import BytesIO
from bz2 import BZ2Decompressor

compressed_data = open('sample.bz2', 'rb').read()

# Create a decompressor object
decompressor = BZ2Decompressor()

# Decompress the data
decompressed_data = decompressor.decompress(compressed_data)

# Print the decompressed data
print(decompressed_data.decode())

# Print the original data
print(open('sample.txt', 'rb').read().decode())

# Test BZ2File
# Open a compressed file in binary mode for reading
with bz2.BZ2File('sample.bz2', 'rb') as file:

    # Decompress the file
    uncompressed_data = file.read()
    
    # Print the decompressed data
    print(uncompressed_data.decode())

# Print the original data
print(open('sample.txt', 'rb').read().decode())

# Test BZ2File with context
