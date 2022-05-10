from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack_from(b'0000')
