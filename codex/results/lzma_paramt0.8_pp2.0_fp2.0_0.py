from lzma import LZMADecompressor
LZMADecompressor().decompress(a)

import array
a = array.array('I', range(5))
print(a)
import binascii
print(binascii.hexlify(a))

import io
s = io.BytesIO()
a = array.array('I', range(5))
a.tofile(s)
print(s.getvalue())

s = io.BytesIO(b'\x01\x00\x00\x00\x02\x00\x00\x00')
a = array.array('I')
a.fromfile(s, 2)
print(len(a), a[0], a[1])
