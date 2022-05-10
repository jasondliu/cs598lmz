import bz2
# Test BZ2Decompressor

# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('test.bz2', 'rb') as f:
    data = f.read()
    print(decompressor.decompress(data))

# Test BZ2File

with bz2.BZ2File('test.bz2', 'rb') as f:
    print(f.read())

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('test.bz2', 'wb') as f:
    f.write(compressor.compress(b'Hello World!'))
    f.write(compressor.flush())

# Test BZ2File

with bz2.BZ2File('test.bz2', 'wb') as f:
    f.write(b'Hello World!')
