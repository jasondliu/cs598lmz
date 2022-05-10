import bz2
# Test BZ2Decompressor

with bz2.BZ2File('data/log.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100 * decompressor.decompress(f.read(100))), b''):
        pass

# Test BZ2Compressor

with bz2.BZ2File('data/log.bz2', 'wb') as f:
    compressor = bz2.BZ2Compressor()
    for data in ['line 1\n', 'line 2\n', 'line 3\n']:
        f.write(compressor.compress(data))
    f.write(compressor.flush())
 
# Test BZ2File

with bz2.BZ2File('data/log.bz2', 'rb') as f:
    for line in f:
        pass

# Test BZ2File

with bz2.BZ2File('data/log.bz2', 'wb') as f:
   
