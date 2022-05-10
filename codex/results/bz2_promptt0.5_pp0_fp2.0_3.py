import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as input:
    with open('data/enwik8.txt', 'wb') as output:
        for block in iter(lambda: input.read(1024 * 1024), b''):
            output.write(decompressor.decompress(block))

!ls -lh data/enwik8.bz2 data/enwik8.txt

# Test BZ2File

with bz2.BZ2File('data/enwik8.bz2', 'rb') as input, open('data/enwik8.txt', 'wb') as output:
    for block in iter(lambda: input.read(1024 * 1024), b''):
        output.write(decompressor.decompress(block))

!ls -lh data/enwik8.bz2 data/enwik8.txt

# Test BZ2File with context manager

with bz2.BZ2File('data/enwik8.
