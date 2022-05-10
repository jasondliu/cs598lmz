from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# decompress data
data = bz2.decompress(data)

# write decompressed data to file
with open('dexter.txt', 'wb') as f:
    f.write(data)

# open file and read first 5 lines
with open('dexter.txt') as f:
    for i in range(5):
        print(f.readline())

#########

import bz2

with bz2.BZ2File('dexter.txt.bz2') as f:
    for i in range(5):
        print(f.readline())

#########

import bz2

with bz2.open('dexter.txt.bz2', 'rt') as f:
    for i in range(5):
        print(f.readline())

#########

import bz2

with bz2.open('dexter.txt.bz2', 'rt') as f1, open('dexter.txt', 'w') as f2
