from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("<H")

def pack(v):
    return s.pack(v)

def unpack(v):
    return s.unpack(v)[0]

def unpack_from(v, o=0):
    return s.unpack_from(v, o)[0]

def pack_into(v, buf, o=0):
    s.pack_into(buf, o, v)

def size():
    return s.size

def format():
    return s.format

def format_size(fmt):
    return Struct.__new__(Struct, fmt).size

def format_unpack(fmt, v):
    return Struct.__new__(Struct, fmt).unpack(v)

def format_unpack_from(fmt, v, o=0):
    return Struct.__new__(Struct, fmt).unpack_from(v, o)

def format_pack(fmt, *args):
    return Struct.__new__(Struct, fmt).pack(*args)


