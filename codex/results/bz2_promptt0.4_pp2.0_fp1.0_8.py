import bz2
# Test BZ2Decompressor
with bz2.BZ2File('data/sample.bz2', 'r') as f:
    decompressor = bz2.BZ2Decompressor()
    for chunk in iter(lambda: f.read(100 * 1024), b''):
        data = decompressor.decompress(chunk)
        print(data)

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
with open('data/sample.bz2', 'wb') as f:
    for data in [b'This is the data', b'which is to be compressed']:
        f.write(compressor.compress(data))
    f.write(compressor.flush())

# Test BZ2File
with bz2.BZ2File('data/sample.bz2', 'rb') as f:
    print(f.read())

with bz2.BZ2File('data/sample.bz2', 'wb') as f:
    f.write(b'This is the data')
    f.write(b
