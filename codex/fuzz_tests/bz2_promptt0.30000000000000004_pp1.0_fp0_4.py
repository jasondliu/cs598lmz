import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as input, open('data/enwik8.txt', 'wb') as output:
    for block in iter(lambda: input.read(100 * 1024), b''):
        output.write(decompressor.decompress(block))
 
# Test BZ2File

with bz2.BZ2File('data/enwik8.bz2', 'rb') as input, open('data/enwik8.txt', 'wb') as output:
    for block in iter(lambda: input.read(100 * 1024), b''):
        output.write(block)
 
# Test BZ2File with seek

with bz2.BZ2File('data/enwik8.bz2', 'rb') as input, open('data/enwik8.txt', 'wb') as output:
    input.seek(100 * 1024)
    for block in iter(lambda: input.read(100 * 1024), b''):
