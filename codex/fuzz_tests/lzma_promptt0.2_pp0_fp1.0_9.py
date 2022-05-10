import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, decompress it, and write the output
with open('data/python.xz', 'rb') as input, \
     open('data/uncompressed.bin', 'wb') as output:
    while True:
        compressor.compress(b'B')
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(decompressor.decompress(chunk))

# Flush the decompressor because we're done
output.write(decompressor.flush())

# Check that the output file is the same as the original
with open('data/python.bin', 'rb') as f:
    original_data = f.read()
with open('data/uncompressed.bin', 'rb') as f:
    uncompressed_data = f.read()
assert original_data == uncompressed_data
 
# Clean up the temporary files
os.unlink('data/uncompressed.bin')
 

