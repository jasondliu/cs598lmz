from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<2c2h'
s.size = 8

def unpack(data):
    return s.unpack(data)

def pack(data):
    return s.pack(*data)
