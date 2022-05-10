from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# Output: b'hello world!\n'

# Compress a file-like object:

import lzma
with open('lorem.txt', 'rb') as input:
    with lzma.open('lorem.txt.xz', 'wt') as output:
        output.write(input.read())

# Decompress a file-like object:

import lzma
with lzma.open('lorem.txt.xz') as input:
    with open('lorem.txt', 'wb') as output:
        output.write(input.read())

# Compress a file:

import lzma
lzma.compress('lorem.txt')

# Decompress a file:

import lzma
lzma.
