from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'H'
s.size = 2

def unpack(fmt, data):
    unpack_from = s.unpack_from
    return unpack_from(data)

def pack(fmt, *args):
    pack = s.pack
    return pack(*args)

def calcsize(fmt):
    calcsize = s.calcsize
    return calcsize(fmt)
