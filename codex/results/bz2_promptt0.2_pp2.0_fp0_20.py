import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with bz2.open('sample.bz2', 'rb') as input:
    with open('uncompressed.txt', 'wb') as output:
        for data in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(data))

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('uncompressed.txt', 'rb') as input:
    with bz2.open('compressed.bz2', 'wb') as output:
        for data in iter(lambda: input.read(100 * 1024), b''):
            output.write(compressor.compress(data))
        output.write(compressor.flush())
 
 
# Test BZ2File

with bz2.open('sample.bz2', 'rt') as input:
    print(input.read())

with bz2.open('compressed.bz2', '
