import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# Get the decompressed data from the decompressor
uncompressed_data = decompressor.unconsumed_tail

# Close the decompressor
decompressor.flush()

# Print the size of the uncompressed data
print('The uncompressed data is {} bytes'.format(len(uncompressed_data)))

# Print the first 300 characters in uncompressed_data
print(uncompressed_data[:300])

# Import the BZ2File class
from bz2 import BZ2File
# Create a BZ2File object
bz2_file = BZ2File('airtravel.csv.bz2')

# Print the number of lines in the uncompressed file
print(len(bz2_file.readlines()))

# Close the BZ2 file
bz2_file.close()

# Import the BZ2File class
from bz2 import BZ2File
# Create a BZ2File object
bz
