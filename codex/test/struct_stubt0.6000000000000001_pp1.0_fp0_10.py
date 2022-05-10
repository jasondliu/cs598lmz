from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'HHI'
s.size = s.calcsize(s.format)

def unpack_from(buffer, offset=0):
    return s.unpack_from(buffer, offset)
