import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress data and write it to a file
with open('test.xz', 'rb') as in_file, \
     open('test.out', 'wb') as out_file:
    for block in iter(lambda: in_file.read(1024 * 1024), b''):
        out_file.write(decompressor.decompress(block))
