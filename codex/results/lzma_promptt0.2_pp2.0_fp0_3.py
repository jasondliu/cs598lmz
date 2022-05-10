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
    original_data = f.read()
with open('data/python.xz', 'rb') as f:
    compressed_data = f.read()
assert decompressor.decompress(compressed_data) == original_data
assert decompressor.flush() == b''
 
# Check that the decompressor object can be reused
with open('data/python.xz', 'rb') as input, open('data/python.txt',
