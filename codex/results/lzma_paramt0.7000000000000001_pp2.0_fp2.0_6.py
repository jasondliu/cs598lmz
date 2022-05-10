from lzma import LZMADecompressor
LZMADecompressor().decompress(b'...')

# Or, decompress as you read:

with open('foo.xz', 'rb') as f:
    with LZMADecompressor() as dc:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            print(dc.decompress(chunk))

# To decompress an entire file, use the decompress() function:

import lzma
lzma.decompress(b'...')

# lzma.decompress() can also decompress files that have multiple concatenated
# compressed streams.

# How to compress a file with LZMA

# The easiest way to use the LZMA compressor is to call the compress() function:

import lzma
lzma.compress(b'...')

# If you want to compress a file using the LZMA library, you can use this code:

with open('file.txt', 'rb') as f:
    with lzma.open('file.txt.xz', 'w') as x
