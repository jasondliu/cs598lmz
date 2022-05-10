from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>2iq'
s.size = s.__sizeof__()
s.pack(0x1, 0x2, 0x3)
