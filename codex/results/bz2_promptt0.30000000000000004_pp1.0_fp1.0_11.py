import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwik9.bz2', 'rb') as input, open('data/enwik9', 'wb') as output:
    for block in iter(lambda: input.read(100 * 1024), b''):
        output.write(decompressor.decompress(block))

# Test BZ2File

with bz2.BZ2File('data/enwik9.bz2', 'rb') as input, open('data/enwik9', 'wb') as output:
    for block in iter(lambda: input.read(100 * 1024), b''):
        output.write(block)
 
# Test bz2.decompress

with open('data/enwik9.bz2', 'rb') as input, open('data/enwik9', 'wb') as output:
    for block in iter(lambda: input.read(100 * 1024), b''):
        output.write(bz2.decompress(block))
 
# Test bz
