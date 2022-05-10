import lzma
# Test LZMADecompressor.
decompressor = lzma.LZMADecompressor()

with open('data/lorem_ipsum.xz', 'rb') as input, \
        open('data/lorem_ipsum.txt', 'wb') as output:
    while True:
        chunk = input.read(64 * 1024)
        if not chunk:
            break
        output.write(decompressor.decompress(chunk))
    output.write(decompressor.flush())

# Test LZMACompressor.
with open('data/lorem_ipsum.txt', 'rb') as input, \
        lzma.open('data/lorem_ipsum.xz', 'wb') as output:
    output.write(input.read())

# Test incremental compression.
compressor = lzma.LZMACompressor()
with open('data/lorem_ipsum.txt', 'rb') as input, \
        open('data/lorem_ipsum_incremental.xz', 'wb') as output:
    while True:
        chunk
