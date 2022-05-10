import bz2
# Test BZ2Decompressor

# Create a BZ2Decompressor object
decompressor = bz2.BZ2Decompressor()

# Decompress the first 3 bytes of the data
print(decompressor.decompress(data[:3]))

# Decompress the rest of the data
print(decompressor.decompress(data[3:]))

# Finish decompression
print(decompressor.flush())

# Test BZ2File

# Open a compressed file in read mode
with bz2.BZ2File('data.bz2', 'r') as file:

    # Print the decompressed data
    print(file.read())

# Open a compressed file in write mode
with bz2.BZ2File('data.bz2', 'w') as file:

    # Write some data
    file.write(b'Hello World!')

# Open a compressed file in append mode
with bz2.BZ2File('data.bz2', 'a') as file:

    # Append some data
    file.write(b'
