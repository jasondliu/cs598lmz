import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/sample.bz2', 'rb') as input:
    with open('data/sample.out', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))

# Test BZ2File

with bz2.BZ2File('data/sample.bz2') as input:
    with open('data/sample.out', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(block)

# Test BZ2File with context manager

with bz2.BZ2File('data/sample.bz2') as input:
    data = input.read()

with open('data/sample.out', 'wb') as output:
    output.write(data)

# Test BZ2File with readline

with bz2.BZ2File('data
