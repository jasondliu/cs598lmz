import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, decompress it, and write the output
with open('lorem.xz', 'rb') as input, open('lorem-decompressed', 'wb') as output:
    while True:
        compressor.compress(b'B')
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(decompressor.decompress(chunk))

# Flush the decompressor because we're done
output.write(decompressor.flush())

# Check that the output file is the same as the original
with open('lorem', 'rb') as f:
    print(f.read() == open('lorem-decompressed', 'rb').read())

# True

# Clean up the output file
os.remove('lorem-decompressed')
 
# Create a compressor object
compressor = lzma.LZMACompressor()

# Read one byte, compress it, and write the output
