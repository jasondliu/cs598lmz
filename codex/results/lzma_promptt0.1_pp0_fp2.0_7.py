import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress one chunk at a time
with open('lorem.xz', 'rb') as input, open('lorem-decompressed', 'wb') as output:
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(decompressor.decompress(chunk))

# Flush the decompressor to get any remaining data
output.write(decompressor.flush())
 
# Test LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Compress one chunk at a time
with open('lorem', 'rb') as input, open('lorem.xz', 'wb') as output:
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(compressor.compress(chunk))

# Flush the compressor to get any remaining data
output.write(
