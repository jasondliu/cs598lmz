import bz2
# Test BZ2Decompressor class and BZ2File class

# Test BZ2Decompressor class
decompressor = bz2.BZ2Decompressor()
with open('test.bz2', 'rb') as f:
    for line in f:
        print(decompressor.decompress(line))

# Test BZ2File class
with bz2.BZ2File('test.bz2', 'rb') as f:
    for line in f:
        print(line.decode('utf-8'))

# Test BZ2File class with context manager
with bz2.open('test.bz2', 'rb') as f:
    for line in f:
        print(line.decode('utf-8'))
