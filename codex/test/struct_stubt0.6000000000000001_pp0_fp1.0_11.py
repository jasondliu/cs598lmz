from _struct import Struct
s = Struct.__new__(Struct)
s
s.__init__(s, '>i')
s.pack(1)
s.unpack(b'\x00\x00\x00\x01')

def pack_into(fmt, buf, offset, *args):
    s = Struct.__new__(Struct)
    s.__init__(s, fmt)
    return s.pack_into(buf, offset, *args)

def unpack_from(fmt, buf, offset=0):
    s = Struct.__new__(Struct)
    s.__init__(s, fmt)
    return s.unpack_from(buf, offset)

def calcsize(fmt):
    s = Struct.__new__(Struct)
    s.__init__(s, fmt)
    return s.size

def pack(fmt, *args):
    s = Struct.__new__(Struct)
    s.__init__(s, fmt)
    return s.pack(*args)

def unpack(fmt, string):
    s = Struct
