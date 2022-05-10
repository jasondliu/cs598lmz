from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>H')

def pack(data):
    return s.pack(data)

def unpack(data):
    return s.unpack(data)[0]

def size():
    return s.size
