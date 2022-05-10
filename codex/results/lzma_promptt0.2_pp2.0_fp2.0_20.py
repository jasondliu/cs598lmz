import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte at a time
with open('data/python.xz', 'rb') as input, open('data/python.txt', 'wb') as output:
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(decompressor.decompress(chunk))
 
# Finish decompression
output.write(decompressor.flush())

# Test LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Read one byte at a time
with open('data/python.txt', 'rb') as input, open('data/python.xz', 'wb') as output:
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(compressor.compress(chunk))
 
# Finish compression
output.write(compressor.flush())
 
# Close the compressor
