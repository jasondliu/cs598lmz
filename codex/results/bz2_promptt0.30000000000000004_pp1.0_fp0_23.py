import bz2
# Test BZ2Decompressor

with bz2.BZ2File('data/sample.bz2', 'rb') as infile:
    with open('data/sample.txt', 'wb') as outfile:
        decompressor = bz2.BZ2Decompressor()
        for data in iter(lambda : infile.read(100 * 1024), b''):
            outfile.write(decompressor.decompress(data))
        outfile.write(decompressor.flush())
 
# Test BZ2Compressor

with open('data/sample.txt', 'rb') as infile:
    with bz2.BZ2File('data/sample.bz2', 'wb') as outfile:
        compressor = bz2.BZ2Compressor()
        for data in iter(lambda : infile.read(100 * 1024), b''):
            outfile.write(compressor.compress(data))
        outfile.write(compressor.flush())
 
# Test BZ2File

with bz2.BZ2File('data/sample.bz
