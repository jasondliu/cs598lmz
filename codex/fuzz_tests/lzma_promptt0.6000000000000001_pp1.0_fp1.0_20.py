import lzma
# Test LZMADecompressor

# Decompress a file
with lzma.open('/home/laura/Documents/Python/Python_Basics/Python_Basics/data/enwik8.lzma', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    decompressed_file = decompressor.decompress(f.read())

# Display some information
print(f'Original size: {len(decompressed_file)}')
print(f'Compressed size: {f.tell()}')
print(f'Compression ratio: {len(decompressed_file)/f.tell()}')

# Show the first 100 characters
print(decompressed_file[:100])

# Create a file-like object to read from
decompressed_file = io.BytesIO(decompressed_file)

# Read the first line
decompressed_file.readline()

# Read the rest of the file
for line in decompressed_file:
    pass

# Test LZMACompressor

# Create a compressor object

