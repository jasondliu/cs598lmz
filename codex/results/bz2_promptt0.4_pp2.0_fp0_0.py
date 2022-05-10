import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as f:
    data = f.read(100)
    print(decompressor.decompress(data))

with open('data/enwik8.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    for chunk in iter(lambda: f.read(100 * 1024), b''):
        data = decompressor.decompress(chunk)
        if data:
            print(data)
        else:
            break

with bz2.open('data/enwik8.bz2', 'r') as f:
    for line in f:
        print(line)
 
# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/enwik8.bz2', 'rb') as f:
    data = f.read(100)
    print(compressor.compress(data
