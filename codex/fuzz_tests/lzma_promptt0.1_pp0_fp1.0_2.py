import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress one chunk at a time
with open('data/python.xz', 'rb') as input, open('data/python.txt', 'wb') as output:
    for chunk in iter(lambda: input.read(4096), b''):
        output.write(decompressor.decompress(chunk))

# Flush the decompressor to get any remaining data
output.write(decompressor.flush())

# Test LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Compress one chunk at a time
with open('data/python.txt', 'rb') as input, open('data/python.xz', 'wb') as output:
    for chunk in iter(lambda: input.read(4096), b''):
        output.write(compressor.compress(chunk))

# Flush the compressor to get any remaining data
output.write(compressor.flush())
 
