import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte at a time
with open('lorem.xz', 'rb') as input:
    with open('lorem.txt', 'wb') as output:
        while True:
            # Read a block of compressed data
            block = input.read(1024)
            if not block:
                break
            # Decompress the block
            uncompressed = decompressor.decompress(block)
            if uncompressed:
                output.write(uncompressed)
            else:
                break
        # Flush the decompressor to get any remaining data
        remaining = decompressor.flush()
        output.write(remaining)
 
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte at a time
with open('lorem.xz', 'rb') as input:
    with open('lorem.txt', 'wb') as output:
        while
