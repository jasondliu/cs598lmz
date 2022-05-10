from _struct import Struct
s = Struct.__new__(Struct)
s.__init__(">I", 4)
s.size

s.pack(7)

s.pack_into(buffer(bytearray(4)), 0, 7)
