import bz2
# Test BZ2Decompressor

# Create a decompressor object
decompressor = bz2.BZ2Decompressor()

# Decompress the data
uncompressed_data = decompressor.decompress(compressed_data)

# Print the length of the uncompressed data
print('The length of the uncompressed data is {}'.format(len(uncompressed_data)))

# Print the first 300 characters in uncompressed_data
print('The first 300 characters in uncompressed_data are {}'.format(uncompressed_data[:300]))

 
# Initialize a new BZ2Decompressor object
decompressor = bz2.BZ2Decompressor()

# Decompress the data chunk by chunk
for chunk in iter(lambda: file.read(100 * 1024), b''):

    # Pass the chunk to the decompressor
    decompressed_chunk = decompressor.decompress(chunk)
    
    # If you don't want to do anything with the decompressed data, you can uncomment the next line
    # and comment out the following one
    # continue
    

