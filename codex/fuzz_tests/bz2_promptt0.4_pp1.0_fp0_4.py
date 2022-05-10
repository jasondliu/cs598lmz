import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# Decompress the entire file
uncompressed_data = bz2.decompress(bz2_data)

# Write the `uncompressed_data` to a file
with open('uncompressed_file.txt', 'wb') as f:
    f.write(uncompressed_data)

# Read in the uncompressed file
with open('uncompressed_file.txt', 'rb') as f:
    uncompressed_data_read = f.read()

# Check that the two are equal
print(uncompressed_data == uncompressed_data_read)

# Using a context manager
with b
