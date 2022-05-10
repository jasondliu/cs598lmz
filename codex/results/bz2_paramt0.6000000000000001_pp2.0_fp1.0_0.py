from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed)

# bz2.BZ2File

import bz2
uncompressor = bz2.BZ2Decompressor()
uncompressed_data = uncompressor.decompress(compressed_data)


# bz2.open()

import bz2
with bz2.open('file.bz2', 'rt') as input:
    for line in input:
        print(line)

import bz2
with bz2.open('file.bz2', 'wt') as output:
    output.write('Contents go here')

import bz2
with bz2.open('file.bz2', 'rt') as input:
    print(input.read())

import bz2
with bz2.open('file.bz2', 'wt') as output:
    output.write('Contents go here')

# zlib

import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len
