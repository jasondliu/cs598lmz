import lzma
# Test LZMADecompressor and LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Compress a single file
with open('file1', 'rb') as input:
    with open('file1.xz', 'wb') as output:
        output.write(compressor.compress(input.read()))

# Flush the compressor to ensure all data is compressed
with open('file2.xz', 'wb') as output:
    output.write(compressor.flush())

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress a single file
with open('file1.xz', 'rb') as input:
    with open('file1.copy', 'wb') as output:
        output.write(decompressor.decompress(input.read()))

# Decompress a file using multiple calls to decompress()
with open('file2.xz', 'rb') as input:
    with open('file2.copy', 'wb') as output:
       
