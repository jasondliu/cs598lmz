import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress one chunk at a time
with open('lorem.xz', 'rb') as input, open('lorem.txt', 'wb') as output:
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        uncompressed = decompressor.decompress(chunk)
        if uncompressed:
            output.write(uncompressed)
        else:
            break

# Flush any remaining data
uncompressed = decompressor.flush()
if uncompressed:
    output.write(uncompressed)

# Check that the output file has the same contents as the input file
with open('lorem.txt', 'rb') as f:
    print(f.read() == lorem)

# Clean up
os.remove('lorem.txt')
os.remove('lorem.xz')

# Test LZMACompressor

# Create a compressor object
compressor = lzma.LZMAC
