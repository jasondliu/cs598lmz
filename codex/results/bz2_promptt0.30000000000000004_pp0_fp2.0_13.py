import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/sample.bz2', 'rb') as input, open('data/sample.out', 'wb') as output:
    for data in iter(lambda: input.read(100 * 1024), b''):
        output.write(decompressor.decompress(data))

# Test BZ2File

with bz2.BZ2File('data/sample.bz2') as input, open('data/sample.out', 'wb') as output:
    for data in iter(lambda: input.read(100 * 1024), b''):
        output.write(data)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor(9)

with open('data/sample.bz2', 'rb') as input, open('data/sample.out', 'wb') as output:
    for data in iter(lambda: input.read(100 * 1024), b''):
        output.write(compressor.compress(data))
    output.
