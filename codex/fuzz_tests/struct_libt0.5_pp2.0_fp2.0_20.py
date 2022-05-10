import _struct
from _struct import *

# This is the same as the struct.pack() function, except that it returns
# a Python object instead of a string.
def pack(fmt, *args):
    return _struct.pack(fmt, *args)

# This is the same as the struct.unpack() function, except that it takes
# a Python object instead of a string.
def unpack(fmt, string):
    return _struct.unpack(fmt, string)

# This is the same as the struct.calcsize() function, except that it takes
# a format string that uses Python objects instead of strings.
def calcsize(fmt):
    return _struct.calcsize(fmt)

# This is the same as the struct.unpack_from() function, except that it takes
# a Python object instead of a string.
def unpack_from(fmt, buffer, offset=0):
    return _struct.unpack_from(fmt, buffer, offset)

# This is the same as the struct.pack_into() function, except that it
