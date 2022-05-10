import bz2
# Test BZ2Decompressor

# Create a BZ2Decompressor object
decompressor = bz2.BZ2Decompressor()

# Decompress the first 3 bytes
print(decompressor.decompress(b'BZh'))

# Read one byte, decompress and print it
print(decompressor.decompress(b'\x41'))

# Decompress the rest
print(decompressor.decompress(b'\x59\x26\x53\x59'))

# Finish decompression
print(decompressor.flush())

# Create a BZ2Decompressor object
decompressor = bz2.BZ2Decompressor()

# Decompress the entire input file
with open('enwik8.bz2', 'rb') as input, open('enwik8.txt', 'wb') as output:
    for data in iter(lambda: input.read(100 * 1024), b''):
        output.write(decompressor.decompress(data))
    output.write(decompressor.flush())


