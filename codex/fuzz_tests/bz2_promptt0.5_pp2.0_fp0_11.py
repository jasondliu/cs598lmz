import bz2
# Test BZ2Decompressor instance
decompressor = bz2.BZ2Decompressor()

# Read compressed file and decompress the data
with bz2.open(filename, 'rb') as file:

    # Get and decompress the first block of data
    block = file.read(1024)
    data = decompressor.decompress(block)

    # Continue until we reach the end of the file
    while len(block) > 0:
        # Print the current block of data
        print(data.decode('utf-8'))

        # Read the next block of compressed data
        block = file.read(1024)

        # Decompress the data
        data = decompressor.decompress(block)

# Print the final block of data
print(data.decode('utf-8'))
# Import BZ2File
from bz2 import BZ2File

# Open the BZ2 file
with BZ2File(filename, 'rb') as file:

    # Loop over each line
    for line in file:

        # Decode the line
        print(line.dec
