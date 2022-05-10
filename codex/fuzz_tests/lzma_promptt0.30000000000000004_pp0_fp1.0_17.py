import lzma
# Test LZMADecompressor

# Create a compressed file
with lzma.open('test.xz', 'wb') as f:
    f.write(b'Hello World!')

# Read the compressed file
with lzma.open('test.xz', 'rb') as f:
    file_content = f.read()

# Decompress the data
decompressor = lzma.LZMADecompressor()
result = decompressor.decompress(file_content)

# Check if the data is intact
print(result)

# Clean up
os.remove('test.xz')

# Output: b'Hello World!'

# Test LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Compress some data
data = b'Hello World!'
result = compressor.compress(data)

# Finish the compression process
result += compressor.flush()

# Write the compressed data to a file
with open('test.xz', 'wb') as f:
    f.write(result)


