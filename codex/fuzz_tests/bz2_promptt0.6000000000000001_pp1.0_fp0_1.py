import bz2
# Test BZ2Decompressor
# In this exercise you are going to decompress a compressed file in memory using a BZ2Decompressor object.

# The file data.bz2 is a compressed version of a book written by Robert C. Martin called Clean Code. You will find the original file in the data folder.

# The file is compressed using the bz2 compression algorithm. The compression ratio is approximately 1.14:1.

# Instructions

# Import the bz2 module.
# Create an instance of BZ2Decompressor.
# Read the compressed file data.bz2 and decompress it.
# Print the first 100 characters of the decompressed file.

# Import the bz2 module
import bz2

# Open the file as binary data
with open('data.bz2', 'rb') as file:
    # Wrap the file with a BZ2Decompressor object
    bz_file = bz2.BZ2Decompressor()
    # Decompress the file
    data = bz_file.decompress(file.read())

# Print the first 100 characters of the decompressed file
