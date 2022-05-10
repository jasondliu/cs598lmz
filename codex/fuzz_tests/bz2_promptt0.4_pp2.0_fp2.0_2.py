import bz2
# Test BZ2Decompressor
#
# This example shows how to use the BZ2Decompressor class to decompress a
# stream of data.

# Open the compressed file
filename = "test.bz2"
f = bz2.BZ2File(filename, 'r')

# Create a decompressing object
decompressor = bz2.BZ2Decompressor()

# Read one compressed block at a time
for block in iter(lambda: f.read(100 * decompressor.decompress_block_size), b''):
    # Decompress the block
    data = decompressor.decompress(block)

    # Do something with the data
    print(data)

# Decompress the rest
data = decompressor.flush()
print(data)

# Close the file
f.close()

# Test BZ2Compressor
#
# This example shows how to use the BZ2Compressor class to compress a stream of
# data.

# Open a file to write the compressed data to
filename = "test.bz2"
f = bz2.B
