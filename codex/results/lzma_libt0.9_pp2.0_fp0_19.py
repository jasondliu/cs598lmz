import lzma
lzma

# gzip.decompress() takes a bytes object and returns a bytes object.
# lzma.decompress() takes a bytes object and returns a bytes object.

# gzip.compress() takes a bytes object and returns a bytes object.
# lzma.compress() takes a bytes object and returns a bytes object.

import zlib

text = b"Hello world, this is a bit of text"

zlib.compress(text)
""  # Returns an empty bytes object b''

zlib.compres
