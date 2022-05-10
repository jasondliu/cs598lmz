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
            data = decompressor.decompress(block)
            # Write the decompressed data
            output.write(data)

# Finish decompression
data = decompressor.flush()
output.write(data)

# Check that the decompressed file is identical to the original
with open('lorem.txt', 'rb') as f:
    original = f.read()
with open('lorem.txt.orig', 'rb') as f:
    decompressed = f.read()
assert original == decompressed
 
# Test LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor
