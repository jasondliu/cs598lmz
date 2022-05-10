import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/text.bz2', 'rb') as input:
    with open('data/uncompressed.txt', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))
        output.write(decompressor.flush())
 
# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/text.txt', 'rb') as input:
    with open('data/compressed.bz2', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(compressor.compress(block))
        output.write(compressor.flush())
 
# Test BZ2File

with bz2.open('data/text.bz2', 'rt') as input:
    with open('data/uncompressed.txt', '
