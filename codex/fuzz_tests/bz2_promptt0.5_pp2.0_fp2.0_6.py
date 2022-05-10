import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/example.bz2', 'rb') as input:
    with open('data/example.out', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/example.bz2', 'rb') as input:
    with open('data/example.out.bz2', 'wb') as output:
        while True:
            block = input.read(1024)
            if not block:
                break
            output.write(compressor.compress(block))

        output.write(compressor.flush())

# Test open

with bz2.open('data/example.bz2', 'rt') as input:
    print(input.read())

print()

with bz2.open('data/example.b
