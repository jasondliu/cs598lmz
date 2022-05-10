import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as input:
    with open('data/enwik8_decompressed.txt', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))
 
# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/enwik8_decompressed.txt', 'rb') as input:
    with open('data/enwik8_compressed.bz2', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(compressor.compress(block))
        output.write(compressor.flush())
 
# Test BZ2File

with bz2.BZ2File('data/enwik8.bz2', 'rb') as input:
    with open('
