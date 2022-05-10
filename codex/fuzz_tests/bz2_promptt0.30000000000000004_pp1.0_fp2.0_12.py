import bz2
# Test BZ2Decompressor

with bz2.BZ2File('../data/sample.bz2') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100 * decompressor.decompress_block_size), b''):
        print(decompressor.decompress(block))

# Test BZ2Compressor

with open('../data/sample.txt', 'rb') as input:
    with bz2.BZ2File('../data/sample.bz2', 'wb') as output:
        compressor = bz2.BZ2Compressor()
        for block in iter(lambda: input.read(100 * compressor.compress_block_size), b''):
            output.write(compressor.compress(block))
        output.write(compressor.flush())

# Test BZ2File

with bz2.BZ2File('../data/sample.bz2') as input:
    print(input.read())

# Test BZ2File

with bz
