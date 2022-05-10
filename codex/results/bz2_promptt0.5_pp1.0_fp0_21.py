import bz2
# Test BZ2Decompressor.
decompressor = bz2.BZ2Decompressor()
with open(bz2_file_path, 'rb') as f:
    for block in iter(lambda: f.read(100 * 1024), b''):
        print(decompressor.decompress(block))
 

# Compress text data with BZ2Compressor.
compressor = bz2.BZ2Compressor()
with open(bz2_file_path, 'wb') as f:
    for i in range(1, 10, 3):
        data = 'test data %d' % i
        print(data)
        f.write(compressor.compress(data.encode()) + compressor.flush())
 
# Test BZ2Compressor.
with open(bz2_file_path, 'rb') as f:
    for block in iter(lambda: f.read(100 * 1024), b''):
        print(decompressor.decompress(block))
