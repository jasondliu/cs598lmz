import lzma
# Test LZMADecompressor

decompressor = lzma.LZMADecompressor()
with open('foo.xz', 'rb') as input, \
        open('foo', 'wb') as output:
    for block in iter(lambda: input.read(64 * 1024), b''):
        output.write(decompressor.decompress(block))
    output.write(decompressor.flush())


# Test LZMACompressor

compressor = lzma.LZMACompressor()
with open('foo.xz', 'wb') as output:
    output.write(compressor.compress(b'Hello'))
    output.write(compressor.flush())


# Test LZMAFile

with lzma.open('foo.xz', 'rb') as input:
    print(input.read())

with lzma.open('foo.xz', 'wt') as output:
    output.write('contents go here')

with lzma.open('foo.xz', 'rt') as input:
    print(input.read())
