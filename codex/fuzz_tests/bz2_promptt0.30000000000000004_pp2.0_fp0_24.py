import bz2
# Test BZ2Decompressor

# Create a decompressor object
decompressor = bz2.BZ2Decompressor()

# Decompress the data
uncompressed_data = decompressor.decompress(compressed_data)

# Print the uncompressed data
print(uncompressed_data)

# Decompress the data
uncompressed_data = bz2.decompress(compressed_data)

# Print the uncompressed data
print(uncompress_data)
 
# Decompress the file
with bz2.open('myfile.bz2', 'rt') as f:
    file_content = f.read()
    print(file_content)
 
# Decompress the file
with bz2.open('myfile.bz2', 'rt') as f:
    file_content = f.readlines()
    print(file_content)
 
# Decompress the file
with bz2.open('myfile.bz2', 'rt') as f:
    for line in f:
        print(line)
 

