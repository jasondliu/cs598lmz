import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with bz2.BZ2File('data/example4.bz2', 'rb') as input:
    for block in iter(lambda: input.read(100 * decompressor.decompress_block.__defaults__[0]), b''):
        print(decompressor.decompress(block))

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with bz2.BZ2File('data/example5.bz2', 'wb') as output:
    for data in [b'This is the wurst, I mean first, line.\n',
                 b'And this is the second line.\n',
                 b'And this is the third line.\n']:
        print(compressor.compress(data))
        output.write(compressor.compress(data))
    print(compressor.flush())
    output.write(compressor.flush())

# Test BZ2File

with bz2.
