from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4

def unpack(data):
    return s.unpack(data)[0]

def pack(data):
    return s.pack(data)
