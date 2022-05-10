import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

# Decompress the data
decompressed_data = decompressor.decompress(compressed_data)

# Print the length of the decompressed data
print('Decompressed Data : {}'.format(len(decompressed_data)))

# Print the decompressed data itself
print(decompressed_data)

# Print the first 500 characters of the decompressed data
print(decompressed_data[:500])

# Define a container string
data = ''

# Loop over each compressed chunk
for chunk in compressed_data_chunks:

    # Decompress the chunk and append the results to the data container
    data += decompressor.decompress(chunk)

# Print the final length of the decompressed data
print('Decompressed Data : {}'.format(len(data)))

# Print the first 500 characters of the decompressed data
print(data[:500])

# Import the BZ2File class
from bz2 import BZ2File

# Create a BZ2
