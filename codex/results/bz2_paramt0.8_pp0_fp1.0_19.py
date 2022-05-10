from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(val)

import io
data = io.BytesIO(b'\x00\x00\x00\x07spam\x00\x08')
data.seek(4)
data.read(4)
data.tell()
data.seek(-3, 2)
data.read(3)

data = io.BytesIO()
data.write(b'abc')
data.seek(0)
data.read(3)

fp = open('somefile.bin', 'wb')
data = io.BytesIO()
data.write(b'abcd\n')
data.seek(0)
fp.write(data.read())
fp.close()
fp = open('somefile.bin', 'rb')
fp.read()

with open('somefile.bin', 'rb') as fp:
    data = fp.read()

import sys, types
class IOMixin:
    if sys.version_info[0] >= 3:
        __str__ = lambda self: self.getvalue()
    else:
        __
