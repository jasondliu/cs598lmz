from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# Output: b'hello'

# Compress a file-like object:

import lzma
with open('lorem.txt', 'rb') as input:
    with lzma.open('lorem-compressed.xz', 'wt') as output:
        output.write(input.read())

# Decompress a file-like object:

import lzma
with lzma.open('lorem-compressed.xz') as input:
    with open('lorem-decompressed.txt', 'wb') as output:
        for line in input:
            output.write(line)

# Compress a file:

import lzma
lzma.compress('lorem.txt', 'lorem-compressed.xz')

#
