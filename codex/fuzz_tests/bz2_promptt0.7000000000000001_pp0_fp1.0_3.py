import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
print(decompressor)

# Decompress
input_file = open('data.bz2', 'rb')
input_file = input_file.read()

# Decompressing bz2 file
output_file = decompressor.decompress(input_file)

# Printing the decompressed data
print(output_file)

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
print(compressor)

# Compress
data = b'This is a test string'
output_file = compressor.compress(data)

# Printing the compressed data
print(output_file)

# Closing the compressor
output_file = compressor.flush()

# Printing the compressed data
print(output_file)

# Compress
data = b'This is a test string'
output_file = bz2.compress(data)

# Printing the compressed data
print(output_file)

# Decompress
output_file = bz2.
