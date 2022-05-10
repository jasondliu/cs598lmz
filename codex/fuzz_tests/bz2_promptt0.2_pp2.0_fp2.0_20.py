import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as f:
    data = f.read(100)
    print(decompressor.decompress(data))

# Test BZ2File

with bz2.BZ2File('data/enwik8.bz2') as f:
    print(f.read(100))

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/enwik8.bz2', 'rb') as f:
    data = f.read(100)
    print(compressor.compress(data))

# Test BZ2File

with bz2.BZ2File('data/enwik8.bz2', 'w') as f:
    f.write(data)
 
# Test BZ2File with context manager

with bz2.BZ2File('data/enwik8.bz2') as f:
    print
