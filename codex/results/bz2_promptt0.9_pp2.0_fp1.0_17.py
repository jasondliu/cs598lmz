import bz2
# Test BZ2Decompressor object    
dec = bz2.BZ2Decompressor()

for line in decompressed_file:
    print(dec.decompress(line))

# Test the entire file

un_compressed_data = bz2.decompress(compressed_file.read())

# Print the uncompressed data
print('The uncompressed data is {} bytes'.format(len(un_compressed_data)))

un_compressed_data[0:1000]
