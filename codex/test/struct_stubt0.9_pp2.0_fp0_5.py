from _struct import Struct
s = Struct.__new__(Struct)
s.size = 4
s._fmt = 'I'
import ctypes
oc = ctypes.pointer(ctypes.c_int())
poc = ctypes.pointer(oc)
import sys
if sys.byteorder == 'big':
    data = bytes.fromhex('01000000')
else:
    data = bytes.fromhex('00000001')
address = data[:s.size]
address, = s.unpack(address)
