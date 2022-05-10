import bz2
# Test BZ2Decompressor

with bz2.BZ2File('data/sample.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100 * 1024), b''):
        data = decompressor.decompress(block)
        if data:
            print(data)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()
with open('data/sample.bz2', 'wb') as f:
    for data in ['a', 'b', 'c', 'd']:
        f.write(compressor.compress(data))
    f.write(compressor.flush())
 
# Test BZ2File

with bz2.BZ2File('data/sample.bz2', 'rb') as f:
    for line in f:
        print(line)
 
# Test open

with bz2.open('data/sample.bz2', 'rb') as f:
    for line in f:

