import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with bz2.open('../data/example4.bz2', 'rb') as input:
    with open('../data/example5.txt', 'wt') as output:
        for block in iter(lambda: input.read(100 * decompressor.decompress_length), b''):
            output.write(decompressor.decompress(block).decode('utf-8'))
 
!ls -l ../data/example*.bz2

!ls -l ../data/example*.txt

!md5sum ../data/example*.bz2

!md5sum ../data/example*.txt

!diff ../data/example5.txt ../data/example5.txt.orig

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('../data/example5.txt', 'rt') as input:
    with bz2.open('../data/example6.bz2', 'wb')
