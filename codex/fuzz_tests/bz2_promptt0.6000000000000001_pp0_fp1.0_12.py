import bz2
# Test BZ2Decompressor by decompressing a file that's already been decompressed
with open('data.txt', 'rb') as input:
    with bz2.BZ2File('data.txt.bz2', 'wb') as output:
        for data in iter(lambda : input.read(100 * 1024), b''):
            output.write(data)
import bz2
with open('data.txt', 'rb') as input:
    decompressor = bz2.BZ2Decompressor()
    with open('data.txt.out', 'wb') as output:
        for block in iter(lambda : input.read(1024), b''):
            output.write(decompressor.decompress(block))
