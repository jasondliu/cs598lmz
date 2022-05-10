import _struct
# Test _struct.Struct. This is pure python
# and should work on any platform.
import array
import binascii
import sys

packed0 = _struct.pack('=h', 1)
packed1 = _struct.pack('=i', 1)
packed2 = _struct.pack('=q', 1)
packed3 = _struct.pack('=l', 1)
packed4 = _struct.pack('<H', 1)
packed5 = _struct.pack('=f', 1)
packed6 = _struct.pack('=d', 1)
packed7 = _struct.pack('=P', 1)
packed8 = _struct.pack('=s', '1')
packed9 = _struct.pack('=c', '1')
packed10 = _struct.pack('=c', 1)


class NewStructTest:

    def pack(self, fmt, vals):
        size = _struct.calcsize(fmt)
        data = _struct.pack(fmt, *vals)
        unpacked = _struct.unpack(fmt, data)
        return size, data, unpacked
