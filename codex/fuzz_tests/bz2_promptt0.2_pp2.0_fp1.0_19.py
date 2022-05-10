import bz2
# Test BZ2Decompressor

with bz2.BZ2File('data/sample.bz2') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100 * decompressor.decompress_block_size), b''):
        data = decompressor.decompress(block)
        print(data)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()
with open('data/sample.txt', 'rb') as f:
    for block in iter(lambda: f.read(100), b''):
        data = compressor.compress(block)
        print(data)
    data = compressor.flush()
    print(data)

# Test BZ2File

with bz2.BZ2File('data/sample.bz2') as f:
    print(f.read())

with bz2.BZ2File('data/sample.bz2', 'w') as f:
    f.write(b'Hello World!')
 

