import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/sample.bz2', 'rb') as input:
    with open('data/sample.out', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))
 
# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/sample.txt', 'rb') as input:
    with open('data/sample.bz2', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(compressor.compress(block))
        output.write(compressor.flush())
 
# Test BZ2File

with bz2.BZ2File('data/sample.bz2', 'rb') as input:
    with open('data/sample.out', 'wb') as output:
        for block in iter(lambda:
