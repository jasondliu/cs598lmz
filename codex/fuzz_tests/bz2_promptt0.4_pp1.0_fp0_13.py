import bz2
# Test BZ2Decompressor
with bz2.BZ2File('../data/Sample.txt.bz2') as f:
    decompressor = bz2.BZ2Decompressor()
    for chunk in iter(lambda: f.read(100 * decompressor.decompress(b'')), b''):
        print(decompressor.decompress(chunk).decode('utf-8'))

# Test BZ2Compressor
with bz2.BZ2File('../data/Sample.txt.bz2', 'w') as f:
    compressor = bz2.BZ2Compressor()
    for data in ['Sample data line 1\n', 'Sample data line 2\n']:
        f.write(compressor.compress(data.encode('utf-8')))
    f.write(compressor.flush())

# Test BZ2File
with bz2.BZ2File('../data/Sample.txt.bz2') as f:
    print(f.read().decode('utf-8'))

# Test BZ2File with
