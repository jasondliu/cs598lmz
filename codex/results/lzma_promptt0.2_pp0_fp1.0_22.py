import lzma
# Test LZMADecompressor

# Create a LZMADecompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte at a time
with open('example.xz', 'rb') as input, open('example.out', 'wb') as output:
    while True:
        # Read a block of compressed data
        block = input.read(1024)
        if not block:
            break

        # Decompress the block
        uncompressed = decompressor.decompress(block)

        # Write the uncompressed data
        output.write(uncompressed)

        # If the decompressor has not reached the end of
        # the compressed data, there is more compressed data
        # to read
        if decompressor.eof:
            break

# Check that the decompressor has reached the end of the
# compressed data
assert decompressor.eof

# Check that the decompressed data is correct
with open('example.out', 'rb') as f:
    data = f.read()
assert data == b'The quick brown fox jumps over the lazy dog.'

