import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Decompress the data
with open('enwik8.lzma', 'rb') as input, open('enwik8.txt', 'wb') as output:
    for data in iter(lambda: input.read(64 * 1024), b''):
        output.write(decompressor.decompress(data))

# Flush the decompressor
output.write(decompressor.flush())

# Check the data integrity
with open('enwik8.txt', 'rb') as f:
    data = f.read()
    print(data[:10])
    print(data[-10:])

# Clean up
os.remove('enwik8.lzma')
os.remove('enwik8.txt')

# Create a LZMA-compressed file
with lzma.open('enwik8.lzma', 'w') as output:
    with open('enwik8', 'rb') as input:
        output.write(input.
