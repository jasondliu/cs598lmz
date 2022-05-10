import bz2
# Test BZ2Decompressor to decompress the compressed file

decompressor = bz2.BZ2Decompressor()

with open('compressed_file.bz2', 'rb') as input, open('decompressed_file.txt', 'wb') as output:
    for data in iter(lambda : input.read(100 * 1024), b''):
        output.write(decompressor.decompress(data))
 
# After decompression, the file is restored to its original state.
# However, the original file is no longer available.
# So, we will have to use the decompressed file to check the final result.

with open('decompressed_file.txt', 'r') as f:
    print(f.read())

# We can see that the file is successfully decompressed.

# The file is now back to its original state.

# The file has now been successfully decompressed.

# The file is now back to its original state.

# The file has now been successfully decompressed.

# The file is now back to its original state.

# The file has now been successfully
