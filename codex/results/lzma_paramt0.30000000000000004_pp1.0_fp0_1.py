from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# Output: b'hello'

# The LZMA algorithm is also used in the .xz file format.
#
# The LZMAFile class provides an interface similar to that of the bz2 module,
# but with support for the .xz format.
#
# The module also provides a simple command line tool for decompressing .xz files.
#
# $ python3 lzma_file.py
# hello
#
# $ python3 lzma_file.py -d < foo.xz
# hello
#
# $ python3 lzma_file.py -d < foo.xz > foo
# $ cmp foo foo.xz
# $

import lzma
import sys

with lzma.open('lzma_file.py.x
