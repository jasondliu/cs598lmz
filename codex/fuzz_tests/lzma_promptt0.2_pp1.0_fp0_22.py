import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress one chunk at a time
with open('data/enwik8.xz', 'rb') as input, open('data/enwik8', 'wb') as output:
    for chunk in iter(lambda: input.read(4096), b''):
        output.write(decompressor.decompress(chunk))

# Flush the decompressor
output.write(decompressor.flush())

# Check the decompressed file size
import os
os.stat('data/enwik8').st_size

# Check the original file size
os.stat('data/enwik8.xz').st_size

# Check the compressed file size
os.stat('data/enwik8.xz').st_size

# Check the compressed file size
os.stat('data/enwik8.xz').st_size

# Check the compressed file size
os.stat('data/enwik8.xz').st_size

# Check the compressed
