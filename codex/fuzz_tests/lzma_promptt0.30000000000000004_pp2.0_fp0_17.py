import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress data and write it to a file
with open('test.xz', 'rb') as in_file, \
     open('test.out', 'wb') as out_file:
    for block in iter(lambda: in_file.read(1024 * 1024), b''):
        out_file.write(decompressor.decompress(block))
    out_file.write(decompressor.flush())

# Check that the output file is the same as the original
with open('test.out', 'rb') as f:
    print(f.read() == open('test', 'rb').read())

# Clean up
os.remove('test.out')

# Test LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Compress data and write it to a file
with open('test', 'rb') as in_file, \
     open('test.xz', 'wb') as
