import lzma
# Test LZMADecompressor

# This test demonstrates how to use LZMADecompressor.

# The LZMADecompressor class can be used to decompress data incrementally.
# This is useful when decompressing data that was not stored in a single
# chunk, such as when decompressing data read from a stream.

# The LZMADecompressor class does not have any public constructor.  Instead,
# use the LZMADecompressor.decompress() class method to create
# LZMADecompressor objects.

# Create a compressor object
decompressor = lzma.LZMADecompressor()

# Decompress data
with open('lzma_compressed.bin', 'rb') as input, \
        open('lzma_uncompressed.bin', 'wb') as output:
    while True:
        block = input.read(1024)
        if not block:
            break
        output.write(decompressor.decompress(block))

# Flush the decompressor by feeding it empty data
output.write(decompressor.
