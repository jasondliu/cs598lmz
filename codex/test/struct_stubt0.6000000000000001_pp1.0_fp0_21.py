from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('<i')
s.unpack(b'\x01\x02\x03\x04')
# (16909060,)
