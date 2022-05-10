import bz2
# Test BZ2Decompressor

# Create a decompressor object
decompressor = bz2.BZ2Decompressor()

# Decompress data
with open('sample.bz2', 'rb') as f:
    file_content = f.read()
    data = decompressor.decompress(file_content)
    
# Print the decompressed data
print(data)

# Create a decompressor object
decompressor = bz2.BZ2Decompressor()

# Decompress data
with open('sample.bz2', 'rb') as f:
    file_content = f.read()
    data = decompressor.decompress(file_content)
    
# Print the decompressed data
print(data)

# Create a decompressor object
decompressor = bz2.BZ2Decompressor()

# Decompress data
with open('sample.bz2', 'rb') as f:
    file_content = f.read()
    data = decompressor.decompress(file_content)
    
# Print the decompressed data
print(
