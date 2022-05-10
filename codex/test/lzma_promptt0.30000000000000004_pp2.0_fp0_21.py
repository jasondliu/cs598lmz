import lzma
# Test LZMADecompressor.

# Create a decompressor object.
decompressor = lzma.LZMADecompressor()

# Read one byte at a time, until there is no more input.
with open('lzma_compressed.xz', 'rb') as input:
    while True:
        # Read a block of compressed data.
        compressed = input.read(1024)
        if not compressed:
            break
        # Decompress the data.
        uncompressed = decompressor.decompress(compressed)
        # Write the uncompressed data.
        with open('lzma_uncompressed.txt', 'ab') as output:
            output.write(uncompressed)

# Flush any remaining data.
