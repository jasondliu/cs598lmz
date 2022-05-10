import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte at a time
with open('lorem_ipsum.xz', 'rb') as input, \
     open('lorem_ipsum.txt', 'wb') as output:
    while True:
        # Read a block of compressed data
        block = input.read(1024)
        if not block:
            break
        # Decompress the block
        data = decompressor.decompress(block)
        # Write the decompressed data to the output file
        output.write(data)

# Check that the decompressor has reached the end of the compressed data
assert decompressor.eof is True

# Decompress the entire file at once
with open('lorem_ipsum.xz', 'rb') as input, \
     open('lorem_ipsum.txt', 'wb') as output:
    data = decompressor.decompress(input.read())
    output.write(data)

# Check that the decompressor has reached the end of
