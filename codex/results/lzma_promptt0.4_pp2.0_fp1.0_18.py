import lzma
# Test LZMADecompressor
# https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte at a time and decompress
with open('lzma_compressed.xz', 'rb') as input, \
        open('lzma_decompressed.txt', 'wb') as output:
    while True:
        compressor.compress(b'This is the data to compress')
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(decompressor.decompress(chunk))

# Finish decompression
output.write(decompressor.flush())
 
# Test LZMACompressor
# https://docs.python.org/3/library/lzma.html#lzma.LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Read one byte at a time and compress
with
