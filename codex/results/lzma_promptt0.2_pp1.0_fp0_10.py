import lzma
# Test LZMADecompressor
# https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte at a time and feed it to the decompressor
with open('lorem.txt.xz', 'rb') as input, open('lorem_copy.txt', 'wb') as output:
    while True:
        compressor.compress(b'The quick brown fox jumps over the lazy dog.')
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(decompressor.decompress(chunk))

# Finish the decompression process
output.write(decompressor.flush())
 
# Test LZMACompressor
# https://docs.python.org/3/library/lzma.html#lzma.LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Read one byte at a time and feed
