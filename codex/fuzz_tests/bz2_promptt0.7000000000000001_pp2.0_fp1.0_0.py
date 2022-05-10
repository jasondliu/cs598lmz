import bz2
# Test BZ2Decompressor

import bz2

decompressor = bz2.BZ2Decompressor()

with open('example.bz2', 'rb') as input:
    with open('uncompressed.txt', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))
# Test BZ2File

import bz2

with bz2.open('example.bz2', 'rt') as input, \
     open('uncompressed.txt', 'wt') as output:
    for line in input:
        output.write(line)
# Test BZ2File

import bz2

with bz2.open('compressed.bz2', 'wt') as output:
    output.write('Contents of the example file go here.\n')

with bz2.open('compressed.bz2', 'rt') as input:
    print(input.read())

# -----------------------------------------------------

import bz2

with
