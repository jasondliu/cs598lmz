import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as f:
    data = f.read(1024)
    while data:
        decompressed = decompressor.decompress(data)
        if decompressed:
            print(decompressed)
        data = f.read(1024)

decompressor.flush()

# Test BZ2File

with bz2.BZ2File('data/enwik8.bz2', 'rb') as f:
    data = f.read(1024)
    while data:
        print(data)
        data = f.read(1024)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/enwik8.bz2', 'rb') as f:
    data = f.read(1024)
    while data:
        compressed = compressor.compress(data)
        if compressed:
            print(compressed)
        data = f.read
