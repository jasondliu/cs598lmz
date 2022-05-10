import lzma
# Test LZMADecompressor

with lzma.open('data/python.xz', 'rb') as f:
    file_content = f.read()

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress the data
result = decompressor.decompress(file_content)

# Print the result
print(result)

# Print the result as a string
print(result.decode('utf-8'))
 
# Print the decompressor's unused_data attribute
print(decompressor.unused_data)

# Print the decompressor's eof attribute
print(decompressor.eof)

# Print the decompressor's needs_input attribute
print(decompressor.needs_input)

# Print the decompressor's needs_input attribute
print(decompressor.needs_input)

# Print the decompressor's needs_input attribute
print(decompressor.needs_input)

# Print the decompressor's needs_input attribute
print(decompressor.needs_input)

# Print the decomp
