import bz2
# Test BZ2Decompressor

with open('sample.log.bz2') as f:
    decompressor = bz2.BZ2Decompressor()
    for line in f:
        line = decompressor.decompress(line)
        if line:
            print(line)

# Test BZ2File

with bz2.BZ2File('sample.log.bz2') as f:
    for line in f:
        print(line)

# Compress with BZ2Compressor

with open('sample.log.bz2', 'wb') as f:
    compressor = bz2.BZ2Compressor()
    for data in [b'line 1\n', b'line 2\n', b'line 3\n']:
        f.write(compressor.compress(data))
    f.write(compressor.flush())
 
with bz2.BZ2File('sample.log.bz2', 'wb') as f:
    for data in [b'line 1\n', b'line 2\n', b'line 3\
