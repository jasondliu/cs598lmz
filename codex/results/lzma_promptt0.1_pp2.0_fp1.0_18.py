import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress one chunk at a time
with open('data/python.xz', 'rb') as input, open('data/python.txt', 'wb') as output:
    for chunk in iter(lambda: input.read(4096), b''):
        output.write(decompressor.decompress(chunk))
 
# Finish decompression
output.write(decompressor.flush())
 
# Check that the output file has the same contents as the original
with open('data/python.txt', 'rb') as f:
    print(f.read() == open('data/python.tar.bz2', 'rb').read())

# True

# Test LZMAFile

# Open an LZMA-compressed file in binary mode
with lzma.open('data/python.xz', 'rb') as input:
    # Read the whole file at once
    file_content = input.read()

# Open a regular uncompressed file for
