import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress the data
with open('data/enwik8.xz', 'rb') as input, open('data/enwik8.txt', 'wb') as output:
    for block in iter(lambda: input.read(64 * 1024), b''):
        output.write(decompressor.decompress(block))

# Flush the decompressor
output.write(decompressor.flush())

# The compressed file is about 1.3 GB
# The decompressed file is about 100 MB
# Let's check the size of the decompressed file
import os

print('The size of the decompressed file is', os.stat('data/enwik8.txt').st_size, 'bytes')

# This is a large file, so we will use the first 1,000,000 bytes for our experiments
# We will use the first 1,000,000 bytes of the file
with open('data/enwik8.txt', 'rb') as input, open('data/enwik
