import lzma
# Test LZMADecompressor

# create a new LZMADecompressor object
decompressor = lzma.LZMADecompressor()

# decompress data
with open('data.xz', 'rb') as input, open('data.txt', 'wb') as output:
    for data in iter(lambda: input.read(64 * 1024), b''):
        output.write(decompressor.decompress(data))

# decompress data
