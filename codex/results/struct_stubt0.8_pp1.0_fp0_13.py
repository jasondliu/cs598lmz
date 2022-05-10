from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<d'

def unpack(fmt, s, offset=0):
    return s.unpack_from(fmt, offset)

def pack(fmt, *args):
    return s.pack(*args)

unpack_from = unpack
pack = pack
calcsize = s.size

# _________________________________________________________________
# struct functions

def unpack(fmt, s, offset=0):
    return s.unpack_from(fmt, offset)

def pack(fmt, *args):
    return s.pack(*args)

unpack_from = unpack
pack = pack
calcsize = s.size

# _________________________________________________________________
# format (minimum size)

# format (minimum size)
def format(fmt, val):
    """
    Formats a number according to the given format string (see ``Struct``).
    """
    return s.pack(fmt, val)

# float (8 bytes)
def float(f, val):
    """
    Formats a floating point number as
