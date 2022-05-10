import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte at a time
with open('enwik8.lzma', 'rb') as input:
    with open('enwik8.txt', 'wb') as output:
        while True:
            chunk = input.read(1024)
            if not chunk:
                break
            output.write(decompressor.decompress(chunk))

# Finish decompression
output.write(decompressor.flush())

# Read all data at once
with open('enwik8.lzma', 'rb') as input:
    with open('enwik8.txt', 'wb') as output:
        output.write(decompressor.decompress(input.read()))

# Read all data at once, using a convenience function
with open('enwik8.lzma', 'rb') as input:
    data = lzma.decompress(input.read())

# Compress data
data = b'Lot of data here'
compressed =
