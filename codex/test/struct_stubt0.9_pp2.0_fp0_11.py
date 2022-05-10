from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<hHI'
s._unpack=Unpack_asciiz
