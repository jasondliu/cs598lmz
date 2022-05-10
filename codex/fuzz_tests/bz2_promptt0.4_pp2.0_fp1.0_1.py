import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('sample.bz2', 'rb') as input:
    with open('sample.out', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('sample.txt', 'rb') as input:
    with open('sample.bz2', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(compressor.compress(block))
        output.write(compressor.flush())
 
# Test open

with bz2.open('sample.bz2', 'rb') as input:
    print(input.read())

with bz2.open('sample.bz2', 'wt') as output:
    output.write('Contents of the example file go here.
