import bz2
# Test BZ2Decompressor and BZ2Compressor
with bz2.BZ2File('lorem.txt.bz2') as source, open('lorem.out', 'wb') as target:
    decompressor = bz2.BZ2Decompressor()
    while True:
        block = source.read(1024)
        if not block:
            break
        target.write(decompressor.decompress(block))
    target.write(decompressor.flush())

with open('lorem.out', 'rb') as source, bz2.BZ2File('lorem2.txt.bz2', 'wb') as target:
    compressor = bz2.BZ2Compressor()
    while True:
        block = source.read(1024)
        if not block:
            break
        target.write(compressor.compress(block))
    target.write(compressor.flush())

import gzip, bz2
# Test all kinds of compression
with gzip.open('lorem.txt.gz', 'rt') as input:
    print(input.
