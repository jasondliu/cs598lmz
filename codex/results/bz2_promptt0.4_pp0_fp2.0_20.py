import bz2
# Test BZ2Decompressor

bz2_decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as input, open('data/enwik8.txt', 'wb') as output:
    for data in iter(lambda : input.read(100 * 1024), b''):
        output.write(bz2_decompressor.decompress(data))
 
# Test BZ2File

with bz2.BZ2File('data/enwik8.bz2', 'rb') as input, open('data/enwik8.txt', 'wb') as output:
    for data in iter(lambda : input.read(100 * 1024), b''):
        output.write(data)
 
# Test BZ2File with context manager

with bz2.BZ2File('data/enwik8.bz2', 'rb') as input, open('data/enwik8.txt', 'wb') as output:
    output.write(input.read())
 
# Test BZ2File with context
