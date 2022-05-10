import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte at a time
with open('lorem.xz', 'rb') as input:
    while True:
        # Read a block of data
        block = input.read(1024)
        if not block:
            break

        # Decompress the block
        data = decompressor.decompress(block)

        # If the decompressor returned any data, print it out
        if data:
            print(data)

# Flush the decompressor to get any remaining data
data = decompressor.flush()
if data:
    print(data)

# Test LZMADecompressor with multiple blocks

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one block at a time
with open('lorem.xz', 'rb') as input:
    while True:
        # Read a block of data
        block = input.read(1024)
        if not block:
            break


