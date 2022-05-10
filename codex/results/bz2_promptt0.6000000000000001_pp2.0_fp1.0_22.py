import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
with open('data/example.bz2', 'rb') as f:
    data = f.read(10)
    print(decompressor.decompress(data))
    data = f.read(10)
    print(decompressor.decompress(data))
    data = f.read(10)
    print(decompressor.decompress(data))

# Test BZ2File
with bz2.BZ2File('data/example.bz2', 'rb') as f:
    for line in f:
        print(line.decode('utf-8'))

# Compress data
data = b'Hello World'
compressed = bz2.compress(data)
with open('data/example.bz2', 'wb') as f:
    f.write(compressed)

# Compress data with an open file
with open('data/example.bz2', 'wb') as f:
    compressor = bz2.BZ2Compressor()
