from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('bbbb')
s.unpack_from(b'\x01\x02\x03\x04')
