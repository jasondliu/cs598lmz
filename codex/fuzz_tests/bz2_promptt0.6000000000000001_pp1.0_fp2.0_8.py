import bz2
# Test BZ2Decompressor
with bz2.BZ2File('test.bz2') as bz2File:
    with open('test.txt', 'w') as testFile:
        decompressor = bz2.BZ2Decompressor()
        for data in iter(lambda : bz2File.read(100 * 1024), b''):
            testFile.write(decompressor.decompress(data))
 
# Test BZ2Compressor
with bz2.BZ2File('test.bz2', 'w') as bz2File:
    with open('test.txt', 'r') as testFile:
        compressor = bz2.BZ2Compressor()
        for data in iter(lambda : testFile.read(100 * 1024), b''):
            bz2File.write(compressor.compress(data))
        bz2File.write(compressor.flush())
 
# Test BZ2File
with bz2.BZ2File('test.bz2') as bz2File:
    with open('test.txt', 'w
