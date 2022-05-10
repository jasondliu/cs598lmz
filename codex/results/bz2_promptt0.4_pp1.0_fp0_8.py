import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('../data/example4.bz2', 'rb') as input:
    for block in iter(lambda: input.read(100 * decompressor.decompress(input.read(100))), b''):
        print(block)

# Iterate over compressed file blocks

import bz2

with bz2.BZ2File('../data/example4.bz2', 'rb') as input:
    for block in iter(lambda: input.read(100), b''):
        print(block)

# Read a compressed file

import bz2

uncompressed_data = bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
print(
