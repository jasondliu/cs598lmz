from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4

def unpack(str):
    return s.unpack(str)
