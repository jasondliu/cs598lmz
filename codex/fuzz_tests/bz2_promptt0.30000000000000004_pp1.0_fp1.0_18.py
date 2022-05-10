import bz2
# Test BZ2Decompressor
with bz2.BZ2File('./data/example.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100 * decompressor.decompress_block_size), b''):
        print(decompressor.decompress(block))

# Test BZ2Compressor
with bz2.BZ2File('./data/example.bz2', 'wb') as f:
    compressor = bz2.BZ2Compressor()
    for data in [b'This is the first line', b'And this is the second line']:
        f.write(compressor.compress(data))
    f.write(compressor.flush())

# Test BZ2File
with bz2.BZ2File('./data/example.bz2', 'rb') as f:
    print(f.read())

with bz2.BZ2File('./data/example.bz2', 'wb') as f:
