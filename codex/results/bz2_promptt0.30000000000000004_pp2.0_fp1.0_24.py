import bz2
# Test BZ2Decompressor

with open('data/test.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100 * 100), b''):
        print(decompressor.decompress(block))

# Test BZ2File

with bz2.BZ2File('data/test.bz2', 'rb') as f:
    for line in f:
        print(line)

# Test BZ2Compressor

with open('data/test.bz2', 'wb') as f:
    compressor = bz2.BZ2Compressor()
    for data in ['line 1', 'line 2', 'line 3']:
        f.write(compressor.compress(data.encode('utf-8')))
    f.write(compressor.flush())

# Test compress() and decompress()

compressed_data = bz2.compress(b'This is some data')
print(compressed_data)

decompressed_data =
