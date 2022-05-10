import bz2
# Test BZ2Decompressor
with open('data/sample.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100 * 1024), b''):
        print(decompressor.decompress(block))

# Test BZ2File
with bz2.open('data/sample.bz2', 'rt') as f:
    print(f.read())

# Test BZ2Compressor
with open('data/sample.bz2', 'wb') as f:
    compressor = bz2.BZ2Compressor()
    for data in ['Hello ', 'World']:
        f.write(compressor.compress(data.encode('utf-8')))
    f.write(compressor.flush())

# Test BZ2File
with bz2.open('data/sample.bz2', 'wt') as f:
    f.write('Hello World')

# Test BZ2File
with bz2.open('data/sample.bz2', '
