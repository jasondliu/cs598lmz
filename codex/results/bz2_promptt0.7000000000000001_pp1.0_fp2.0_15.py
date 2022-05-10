import bz2
# Test BZ2Decompressor on the data from the previous example.

decompressor = bz2.BZ2Decompressor()

decompressor.decompress(compressed)

decompressor.flush()

# b'This is the original text.'
# Note that we only had to call decompress() once because we provided all of the compressed data in the first call.

# If we had more data to decompress, we could repeatedly call decompress() with more compressed data until the entire file had been decompressed.
# Let’s try that with a larger file.

# Read the entire compressed file into a single bytes object.
with bz2.BZ2File('lorem.txt.bz2', 'rb') as input:
    compressed = input.read()

# Create a file object to write the decompressed data to.
with open('uncompressed.txt', 'wb') as output:
    decompressor = bz2.BZ2Decompressor()

    # Decompress the data.
    for block in iter(lambda : compressed, b''):
        output.write(decompressor.
