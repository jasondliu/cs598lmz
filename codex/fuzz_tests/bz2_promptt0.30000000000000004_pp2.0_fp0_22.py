import bz2
# Test BZ2Decompressor

# Create a decompressor object
decompressor = bz2.BZ2Decompressor()

# Decompress the first 3 characters
print(decompressor.decompress(b'BZh'))

# Decompress the next 5 characters
print(decompressor.decompress(b'91YY'))

# Finish decompression
print(decompressor.flush())

# Decompress the entire file
with bz2.open('example.bz2', 'rb') as input:
    decompressed_data = decompressor.decompress(input.read())
    print(decompressed_data)

# Decompress an incomplete file
with bz2.open('example.bz2', 'rb') as input:
    for block in iter(lambda: input.read(100), b''):
        decompressed_data = decompressor.decompress(block)
        print(decompressed_data)

# Decompress an entire file using a decompressor object
with bz2.open('example.bz2', 'rb') as
