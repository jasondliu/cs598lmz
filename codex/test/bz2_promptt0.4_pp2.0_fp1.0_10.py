import bz2
# Test BZ2Decompressor

d = bz2.BZ2Decompressor()

with open('example.bz2', 'rb') as f:
    for data in iter(lambda: f.read(100 * 1024), b''):
        rv = d.decompress(data)
        if rv:
            print(rv)

# Test BZ2File

with bz2.BZ2File('example.bz2') as f:
    for line in f:
        print(line)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('example.bz2', 'rb') as f:
    for data in iter(lambda: f.read(100 * 1024), b''):
        rv = compressor.compress(data)
        if rv:
            print(rv)
    rv = compressor.flush()
