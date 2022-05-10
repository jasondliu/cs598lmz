import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/example.bz2', 'rb') as input:
    with open('data/example.txt', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))

print(open('data/example.txt').read())

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/example.txt', 'rb') as input:
    with open('data/example.bz2', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(compressor.compress(block))
        output.write(compressor.flush())

print(open('data/example.bz2', 'rb').read())

# Test BZ2File

with bz2.BZ2File('data/example.bz2') as
