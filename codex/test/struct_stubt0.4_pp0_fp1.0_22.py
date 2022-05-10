from _struct import Struct
s = Struct.__new__(Struct)
s.format = '4s4s'
s.size = 8

def pack(fmt, *args):
    s.format = fmt
    return s.pack(*args)

def unpack(fmt, *args):
    s.format = fmt
    return s.unpack(*args)

def calcsize(fmt):
    s.format = fmt
    return s.size

# ____________________________________________________________

def pack_into(fmt, buffer, offset, *args):
    if len(buffer) < offset + calcsize(fmt):
        raise error("buffer too small for pack_into")
    s.format = fmt
    s.pack_into(buffer, offset, *args)

def unpack_from(fmt, buffer, offset=0):
    s.format = fmt
    return s.unpack_from(buffer, offset)

# ____________________________________________________________

def iter_unpack(fmt, buffer):
    s.format = fmt
    return s.iter_unpack(buffer)

# ________________________________________________________
