import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, decompress it, and write the result
with open('lorem.txt.xz', 'rb') as input, \
     open('lorem.txt', 'wb') as output:
    while True:
        chunk = input.read(1)
        if not chunk:
            break
        result = decompressor.decompress(chunk)
        if result:
            output.write(result)
    output.write(decompressor.flush())
 
# Test LZMACompressor

# Create a compressor object
compressor = lzma.LZMACompressor()

# Read one byte, compress it, and write the result
with open('lorem.txt', 'rb') as input, \
     open('lorem.txt.xz', 'wb') as output:
    while True:
        chunk = input.read(1)
        if not chunk:
            break
        result = compressor.compress(chunk)
        if result
