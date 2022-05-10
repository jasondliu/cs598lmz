import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
with open('data/enwik8', 'rb') as input, open('data/enwik8.out', 'wb') as output:
    for block in iter(lambda: input.read(64 * 1024), b''):
        output.write(decompressor.decompress(block))
    output.write(decompressor.flush())

# Test LZMACompressor
compressor = lzma.LZMACompressor()
with open('data/enwik8', 'rb') as input, open('data/enwik8.xz', 'wb') as output:
    output.write(compressor.compress(input.read()))
    output.write(compressor.flush())

# Test LZMADecompressor.readinto()
decompressor = lzma.LZMADecompressor()
with open('data/enwik8', 'rb') as input, open('data/enwik8.out', 'wb') as output:
    while True:
        buf = decompressor
