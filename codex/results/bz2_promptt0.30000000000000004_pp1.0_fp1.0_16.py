import bz2
# Test BZ2Decompressor

with bz2.BZ2File('../data/sample.bz2') as f:
    for line in f:
        print(line)

# Test BZ2Compressor

with bz2.BZ2File('../data/sample.bz2', 'wb') as f:
    f.write(b'Hello World')

# Test BZ2Compressor and BZ2Decompressor

with open('../data/sample.txt', 'rb') as input:
    with bz2.BZ2File('../data/sample.bz2', 'wb') as output:
        compressor = bz2.BZ2Compressor()
        for block in iter(lambda: input.read(64), b''):
            output.write(compressor.compress(block))
        output.write(compressor.flush())

with bz2.BZ2File('../data/sample.bz2', 'rb') as input:
    with open('../data/sample.txt.out', 'wb') as output:
        decompressor = bz
