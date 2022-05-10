from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>2iq'
s.size = s.__sizeof__()
