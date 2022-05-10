import lzma
# Test LZMADecompressor

decompressor = lzma.LZMADecompressor()
with open('foo.xz', 'rb') as input, \
        open('foo', 'wb') as output:
    for block in iter(lambda: input.read(64 * 1024), b''):
        output.write(decompressor.decompress(block))
