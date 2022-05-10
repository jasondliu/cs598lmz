import bz2
# Test BZ2Decompressor

with bz2.BZ2File('data/test.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda : f.read(100 * 1024), b''):
        data = decompressor.decompress(block)
        if data:
            print(data)

# Test BZ2File

with bz2.BZ2File('data/test.bz2', 'rb') as f:
    for line in f:
        print(line)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()
with open('data/test.bz2', 'wb') as f:
    f.write(compressor.compress(b'This is the first line.\n'))
    f.write(compressor.compress(b'This is the second line.\n'))
    f.write(compressor.compress(b'This is the third line.\n'))
    f.write(compressor.
