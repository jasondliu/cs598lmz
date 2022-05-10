import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress one chunk at a time
with open('compressed_file.xz', 'rb') as input, open('decompressed_file', 'wb') as output:
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(decompressor.decompress(chunk))

# Flush the decompressor by feeding it empty bytes
output.write(decompressor.flush())
 
# Test LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Compress one chunk at a time
with open('decompressed_file', 'rb') as input, open('compressed_file.xz', 'wb') as output:
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(compressor.compress(chunk))

# Flush the compressor by feeding it empty
