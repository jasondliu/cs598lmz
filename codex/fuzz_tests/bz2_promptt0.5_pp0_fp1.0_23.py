import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with bz2.open('sample.bz2', 'rb') as input:
    with open('sample.out', 'wb') as output:
        for data in iter(lambda : input.read(100 * 1024), b''):
            output.write(decompressor.decompress(data))

        output.write(decompressor.flush())

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('sample.out', 'rb') as input:
    with bz2.open('sample.bz2', 'wb') as output:
        for data in iter(lambda : input.read(100 * 1024), b''):
            output.write(compressor.compress(data))

        output.write(compressor.flush())

# Test open()

with bz2.open('sample.bz2', 'rb') as input:
    print(input.read())

# Test compress() and decompress()

uncompressed
