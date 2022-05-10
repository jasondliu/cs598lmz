import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()
# Read the compressed file
with open('enwik9.xz', 'rb') as input, open('enwik9-lzma.txt', 'wb') as output:
    # Read 1 MB at a time
    for block in iter(lambda: input.read(1024 * 1024), b''):
        output.write(decompressor.decompress(block))
    # Flush the decompressor
    output.write(decompressor.flush())
 
# Close the files
input.close()
output.close()
 
# Print the decompressed file size
print('Decompressed size:', os.path.getsize('enwik9-lzma.txt'))

# Test LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()
# Read the decompressed file
with open('enwik9-lzma.txt', 'rb') as input, open('enwik9-lzma.xz', '
