from _struct import Struct
s = Struct.__new__(Struct)
"""

def _make_struct(format):
    """Create a struct object with the specified format.

    This function is used by the struct module to create a struct object
    for the format string specified by the user.

    """
    return Struct.__new__(Struct, format)

_clearcache = Struct.__init__.__code__.co_clear_cache

def calcsize(fmt):
    """Return size in bytes of the struct described by the format string fmt."""
    return _clearcache(_struct.calcsize(fmt))

def pack(fmt, *args):
    """Pack the values v1, v2, ... according to the format string fmt.

    The return value is a bytes object encoding the values.

    """
    return _clearcache(_struct.pack(fmt, *args))

def unpack(fmt, string):
    """Unpack the string (presumably packed by pack(fmt, ...)) according to
    the format string fmt.  The return value is a tuple even if it contains
    exactly one item. 
