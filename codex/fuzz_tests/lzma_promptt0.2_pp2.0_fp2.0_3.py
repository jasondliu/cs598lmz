import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte at a time
with open('lorem.xz', 'rb') as input:
    while True:
        # Read a block of compressed data
        compressed = input.read(1024)
        if not compressed:
            break
        # Decompress the block
        data = decompressor.decompress(compressed)
        if data:
            # Do something with the decompressed data
            print(data)
        else:
            # End of data
            break

# Flush the decompressor to get any remaining data
data = decompressor.flush()
if data:
    print(data)

# Test LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Read one byte at a time
with open('lorem.txt', 'rb') as input:
    with open('lorem.xz', 'wb') as output:
        while True:
            # Read a block of data
           
