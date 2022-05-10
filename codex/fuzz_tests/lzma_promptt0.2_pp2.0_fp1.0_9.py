import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress data
with open('data/enwik8.xz', 'rb') as input, open('data/enwik8.txt', 'wb') as output:
    for block in iter(lambda: input.read(64 * 1024), b''):
        output.write(decompressor.decompress(block))

# Flush the decompressor
output.write(decompressor.flush())
 
# Test LZMAFile

# Open a compressed file
with lzma.open('data/enwik8.xz') as input:
    # Open a regular file for writing
    with open('data/enwik8.txt', 'wb') as output:
        # Copy the data
        shutil.copyfileobj(input, output)
 
# Test LZMAFile with context manager

# Open a compressed file
with lzma.open('data/enwik8.xz') as input:
    # Open a regular file for writing
    with
