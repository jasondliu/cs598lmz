import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_content)

# Decompress the data
decompressed_data = bz2.decompress(compressed_content)

# Write the decompressed data
with gzip.open('decompressed_file.txt', 'wb') as outfile:
    outfile.write(decompressed_data)

# Print the output of the decompression
print(decompressed_data.decode('utf-8'))
 

# Decompress the data using bz2.decompress()
decompressed_data = bz2.decompress(compressed_content)

# Print the result
print(decompressed_data)
 

# Initialize a new file decompression object using gzip
with gzip.open('text.txt.gz', 'rb') as file:
    # Print the decompressed file object
    print(file.read())
 

# Import gzip and shutil modules
import gzip
import shutil


