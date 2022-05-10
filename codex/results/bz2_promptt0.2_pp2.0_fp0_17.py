import bz2
# Test BZ2Decompressor

# create a decompressor object
decompressor = bz2.BZ2Decompressor()

# read the compressed file
with open('data/compressed-file.bz2', 'rb') as file:
    compressed_data = file.read()

# decompress the compressed data
data = decompressor.decompress(compressed_data)

# display the decompressed data
print(data.decode('utf-8'))

# close the decompressor object
decompressor.close()

# Test BZ2File

# open a compressed file
with bz2.BZ2File('data/compressed-file.bz2', 'rb') as file:
    # read the compressed data
    compressed_data = file.read()

# display the compressed data
print(compressed_data)

# open a compressed file
with bz2.BZ2File('data/compressed-file.bz2', 'rb') as file:
    # read the decompressed data
    data = file.read()

# display the decompressed data

