from _struct import Struct
s = Struct.__new__(Struct)
s.s = '<h'
s.pack(1)
'\x00\x01'
bytes(s.pack(1))
b'\x00\x01'
b = bytes(s.pack(1))
b
b'\x00\x01'
b[0]
0
len(b)
2
b[0] = 0xFF
b
b'\xff\x01'


# stdlib
from ctypes import Structure, c_int
class S(Structure):_fields_ = [('a', c_int)]
