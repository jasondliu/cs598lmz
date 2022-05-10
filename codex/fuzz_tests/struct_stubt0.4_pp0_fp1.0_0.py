from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>hhl'
s.size = s.calcsize(s.format)

def unpack_from(buffer, offset=0):
    return s.unpack_from(buffer, offset)

def pack_into(buffer, offset, *values):
    return s.pack_into(buffer, offset, *values)

def unpack(buffer):
    return s.unpack(buffer)

def pack(*values):
    return s.pack(*values)

def size():
    return s.size

def format():
    return s.format

def calcsize(format):
    return s.calcsize(format)
