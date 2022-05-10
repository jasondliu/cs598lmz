import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress a file-like object
with open('lorem.txt.xz', 'rb') as input, \
     open('lorem_decompressed.txt', 'wb') as output:
    for block in iter(lambda: input.read(64 * 1024), b''):
        output.write(decompressor.decompress(block))

# Flush the decompressor
output.write(decompressor.flush())

# Decompress a single block of data
with open('lorem.txt.xz', 'rb') as input:
    block = input.read(1024)
    print(decompressor.decompress(block))

# Decompress a block of data that is not a multiple of the block size
with open('lorem.txt.xz', 'rb') as input:
    block = input.read(1024)
    print(decompressor.decompress(block, max_length=512))

# Decompress a
