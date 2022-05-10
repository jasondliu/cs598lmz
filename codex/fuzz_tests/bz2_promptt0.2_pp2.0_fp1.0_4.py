import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with bz2.open('data/example4.bz2', 'rb') as input:
    with open('data/uncompressed.txt', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))

print(open('data/uncompressed.txt', 'rt').read())

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/uncompressed.txt', 'rb') as input:
    with bz2.open('data/compressed.bz2', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(compressor.compress(block))
        output.write(compressor.flush())

print(open('data/compressed.bz2', 'rb').read())

# Test BZ2File

