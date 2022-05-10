import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with bz2.BZ2File('data/sample.bz2', 'rb') as input:
    for block in iter(lambda: input.read(100 * 1024), b''):
        output = decompressor.decompress(block)
        if output:
            print(output)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/sample.txt', 'rb') as input, \
        bz2.BZ2File('data/sample.bz2', 'wb') as output:
    for block in iter(lambda: input.read(100 * 1024), b''):
        output.write(compressor.compress(block))

    output.write(compressor.flush())
 
# Test BZ2File

with bz2.BZ2File('data/sample.bz2', 'rb') as input:
    print(input.read())
 
# Test open

with bz2.open
