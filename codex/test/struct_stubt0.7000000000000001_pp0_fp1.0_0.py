from _struct import Struct
s = Struct.__new__(Struct)
s.size = Struct.size
def encode(value):
    return s.pack(value)

def decode(buffer):
    return s.unpack(buffer)[0]
