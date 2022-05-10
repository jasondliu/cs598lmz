from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)
 
# This returns you back your original string!

# Decompressing data
with open('sample.bz2', 'rb') as f:
    file_content = f.read()

decompressor = BZ2Decompressor()

original_data = decompressor.decompress(file_content)

len(original_data) # should be equal with the uncompressed data

# Decompressing file
with open('sample.bz2') as input_file, open('destinationfile.txt', 'wb') as output_file:
    decompressor = BZ2Decompressor()

    for data in iter(lambda: input_file.read(100 * 1024), b''):
        output_file.write(decompressor.decompress(data))

# NOTE: In case of bz2:
# The bz2 module does not support incremental compression.
# You need to read the entire file at once.

# Calculate the amount of extra space needed for compression.
import bz2

uncompressed_data =
