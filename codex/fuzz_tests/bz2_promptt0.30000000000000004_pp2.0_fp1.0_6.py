import bz2
# Test BZ2Decompressor
# https://docs.python.org/3/library/bz2.html

# Create a BZ2Decompressor object
decompressor = bz2.BZ2Decompressor()

# Decompress the data
uncompressed_data = decompressor.decompress(compressed_data)

# Print the length of the uncompressed data
print('The length of the uncompressed data is {}'.format(len(uncompressed_data)))

# Print the first 500 characters in uncompressed_data
print(uncompressed_data[:500])

# Read the compressed file
with bz2.open('eswiki-latest-pages-articles.xml.bz2', 'rb') as file:
    compressed_data = file.read()

# Decompress the data
uncompressed_data = bz2.decompress(compressed_data)

# Write the decompressed data to a file
with open('eswiki-latest-pages-articles.xml', 'wb') as file:
    file.write(uncompressed_data)
 
# Read
