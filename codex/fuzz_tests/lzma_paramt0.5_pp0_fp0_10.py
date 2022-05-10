from lzma import LZMADecompressor
LZMADecompressor()

# uncompress
with open('data/compressed.xz', 'rb') as input, \
     open('data/uncompressed.txt', 'wb') as output:
    decompressor = LZMADecompressor()
    for block in iter(lambda: input.read(64 * 1024), b''):
        output.write(decompressor.decompress(block))
    output.write(decompressor.flush())

# compress
with open('data/uncompressed.txt', 'rb') as input, \
     lzma.open('data/compressed.xz', 'wb') as output:
    output.write(input.read())

# use LZMAFile
with lzma.open('data/compressed.xz') as f:
    text = f.read()

# use LZMAFile with context manager
with lzma.open('data/compressed.xz') as f:
    text = f.read()

# use LZMAFile with context manager
with lzma.open('data/compressed.
