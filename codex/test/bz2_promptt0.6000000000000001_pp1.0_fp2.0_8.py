import bz2
# Test BZ2Decompressor
with bz2.BZ2File('test.bz2') as bz2File:
    with open('test.txt', 'w') as testFile:
        decompressor = bz2.BZ2Decompressor()
