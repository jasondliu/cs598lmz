import lzma
lzma.LZMADecompressor()

import pyximport
pyximport.install()

from cython_lzma import LZMADecompressor

import time

#
# Test LZMA
#

f = open('../../test/testdata/xz/alice29.txt.xz', 'rb')

magic = f.read(6)
assert magic == b'\xfd7zXZ\x00'

stream_flags = f.read(2)
assert stream_flags == b'\x00\x00'

check = f.read(4)
assert check == b'\x00\x00\x00\x00'

#
# LZMA Stream Header
#

lzma_properties = f.read(5)

lc, lp, pb, dict_size = struct.unpack('<BHBH', lzma_properties)

dict_size = 2**dict_size

assert lc == 3
assert lp == 0
assert pb == 2
assert
