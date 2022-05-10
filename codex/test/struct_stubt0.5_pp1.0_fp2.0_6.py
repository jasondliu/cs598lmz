from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>h')
s.unpack_from(b'\x00\x01', 0)
(1,)
