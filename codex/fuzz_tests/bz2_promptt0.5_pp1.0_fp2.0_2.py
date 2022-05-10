import bz2
# Test BZ2Decompressor class
decompressor = bz2.BZ2Decompressor()

with open('data/example4.bz2', 'rb') as input, open('data/uncompressed.txt', 'wb') as output:
    for data in iter(lambda: input.read(100 * 1024), b''):
        output.write(decompressor.decompress(data))
import bz2
# Test BZ2Decompressor class
decompressor = bz2.BZ2Decompressor()

with open('data/example4.bz2', 'rb') as input, open('data/uncompressed.txt', 'wb') as output:
    for data in iter(lambda: input.read(100 * 1024), b''):
        output.write(decompressor.decompress(data))
import bz2
# Test BZ2Decompressor class
decompressor = bz2.BZ2Decompressor()

with bz2.open('data/example4.bz2', 'rb') as input, open('data/uncompressed.txt
