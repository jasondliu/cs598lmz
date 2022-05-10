import bz2
# Test BZ2Decompressor

with open('test.txt.bz2', 'rb') as input:
    decompressor = bz2.BZ2Decompressor()
    with open('test.txt', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))
        output.write(decompressor.flush())
# Test BZ2Compressor

with open('test.txt', 'rb') as input:
    compressor = bz2.BZ2Compressor()
    with open('test.txt.bz2', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(compressor.compress(block))
        output.write(compressor.flush())
# Test BZ2File

with bz2.BZ2File('test.txt.bz2', 'rb') as input:
    with open('test.txt', 'wb') as output:
        output.write(input.read
