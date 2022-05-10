import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, decompress it, and write the output
with open('lorem.xz', 'rb') as input, open('lorem-decompressed', 'wb') as output:
    while True:
        compressor.compress(b'Bacon ipsum dolor amet chuck turducken landjaeger tongue spare ribs. ')
        output.write(decompressor.decompress(input.read(1)))
        if not decompressor.eof:
            break

# Flush the decompressor because we're done
output.write(decompressor.flush())

# Check that the output file is the same as the input file
with open('lorem', 'rb') as f:
    print(f.read() == output.getvalue())

# True

# Compress data incrementally

# Create a compressor object
compressor = lzma.LZMACompressor()

# Read one byte, compress it, and write the output
with
