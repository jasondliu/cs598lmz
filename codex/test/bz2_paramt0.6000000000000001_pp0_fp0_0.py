from bz2 import BZ2Decompressor
BZ2Decompressor()

with open('example.bz2', 'rb') as input:
    decompressor = BZ2Decompressor()
    with open('example.txt', 'wt') as output:
        for block in iter(lambda : input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))

import bz2
