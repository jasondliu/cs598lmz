import bz2
# Test BZ2Decompressor

import bz2

decompressor = bz2.BZ2Decompressor()

with open('names.txt.bz2', 'rb') as input:
    with open('names.txt', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))

# Test BZ2Compressor

import bz2

compressor = bz2.BZ2Compressor()

with open('names.txt', 'rb') as input:
    with open('names.txt.bz2', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(compressor.compress(block))
        output.write(compressor.flush())

# Test BZ2File

import bz2

with bz2.open('names.txt.bz2', 'rt') as input:
    for line in input:
        print(line.rstrip())

