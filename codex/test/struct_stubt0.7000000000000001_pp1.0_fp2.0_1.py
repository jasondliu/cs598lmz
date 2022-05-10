from _struct import Struct
s = Struct.__new__(Struct)
s.size = Struct.size
s.format = Struct.format

def _unpack(data):
    return s.unpack(data)[0]

def _pack(number):
    return s.pack(number)
