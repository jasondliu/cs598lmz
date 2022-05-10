import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/sample.bz2', 'rb') as f, open('data/sample.txt', 'wb') as outfile:
    for data in iter(lambda : f.read(100 * 1024), b''):
        outfile.write(decompressor.decompress(data))

# Test BZ2File

with bz2.BZ2File('data/sample.bz2', 'rb') as f, open('data/sample.txt', 'wb') as outfile:
    for data in iter(lambda : f.read(100 * 1024), b''):
        outfile.write(data)
 
# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/sample.txt', 'rb') as f, open('data/sample_compressed.bz2', 'wb') as outfile:
    for data in iter(lambda : f.read(100 * 1024), b''):
        outfile.write(comp
