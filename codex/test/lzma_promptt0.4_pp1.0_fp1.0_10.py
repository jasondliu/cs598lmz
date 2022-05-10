import lzma
# Test LZMADecompressor

# Create a file with a known content
with open('/tmp/lzma_data', 'wb') as f:
    f.write(b'Hello, world!')

# Compress the file
with open('/tmp/lzma_data', 'rb') as f:
    compressed = lzma.compress(f.read())

# Write the compressed file
with open('/tmp/lzma_data.xz', 'wb') as f:
    f.write(compressed)

# Read the compressed file
with open('/tmp/lzma_data.xz', 'rb') as f:
    compressed = f.read()

# Decompress the file
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)

# Verify the content
print(decompressed)

# Cleanup
