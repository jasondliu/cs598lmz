from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')

def pack(fmt, *args):
    return s.pack(fmt, *args)

def unpack(fmt, *args):
    return s.unpack(fmt, *args)

def calcsize(fmt):
    return s.calcsize(fmt)

# --- Struct 'L' support

def pack_long(fmt, *args):
    return s.pack(fmt, *args)

def unpack_long(fmt, *args):
    return s.unpack(fmt, *args)

def calcsize_long(fmt):
    return s.calcsize(fmt)

# --- End of emulation

def unpack_from(fmt, buffer, offset=0):
    return s.unpack_from(fmt, buffer, offset)

def pack_into(fmt, buffer, offset, *args):
    return s.pack_into(fmt, buffer, offset, *args)
