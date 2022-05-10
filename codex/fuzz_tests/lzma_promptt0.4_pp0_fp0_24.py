import lzma
# Test LZMADecompressor

# Make a compressor and decompressor object
decompressor = lzma.LZMADecompressor()

# Read some data to decompress
with open('sample.lzma', 'rb') as input:
    compressed_data = input.read()

# Decompress the data
data = decompressor.decompress(compressed_data)

# Display the decompressed data
print(data)

# Decompress files
with open('sample.lzma', 'rb') as input, open('sample.out', 'wb') as output:
    decompressor = lzma.LZMADecompressor()
    for block in iter(lambda: input.read(64 * 1024), b''):
        output.write(decompressor.decompress(block))
    output.write(decompressor.flush())

# Decompress streams
with open('sample.lzma', 'rb') as input, open('sample.out', 'wb') as output:
    decompressor = lzma.LZMADecompressor()
    while True:

