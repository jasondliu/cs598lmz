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
            text = decompressor.decompress(block)
            # Write the decompressed data
            output.write(text)

# Flush the decompressor
text = decompressor.flush()
output.write(text)

# Close the files
input.close()
output.close()
 
# Test LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Read one byte at a time
with open('lorem.txt', 'rb') as input:
    with open('lorem.xz', 'wb') as output:
        while True:
            # Read
