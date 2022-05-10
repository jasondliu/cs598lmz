from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# ##############################################################################

# lzma.open()

import lzma

with lzma.open("/tmp/foo.xz") as f:
    file_content = f.read()

# ##############################################################################

# lzma.compress()

import lzma

lzma.compress("Hello world!")

# ##############################################################################

# lzma.decompress()

import lzma

lzma.decompress(b"\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x00\x00\x04")

# ##############################################################################

# lzma.compress() and lzma.decompress()

import lzma

data = b"Hello world!"
compressed = lzma
