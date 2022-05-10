from _struct import Struct
s = Struct.__new__(Struct)
s.__doc__ = """This class is used to create packing and unpacking
functions for the C {type} type."""

def new_Struct(*args):
    """Returns a new instance of the Struct class which writes and reads
    bytes in standard C struct format according to the format string that
    is passed to its constructor."""
    try:
        n = len(args)
        if n == 1:
            obj = s.__new__(Struct)
            obj.format = args[0]
            obj.size = struct.calcsize(obj.format)
            obj.unpack = Struct.__dict__['unpack']
            obj.pack_into = Struct.__dict__['pack_into']
            return obj
        if n == 2:
            # See issue 16955
            raise TypeError
    except (ValueError, TypeError):
        raise TypeError("Struct() takes exactly 1 argument")
    raise TypeError("Struct() takes at most 2 positional arguments")

struct.Struct = Struct
struct.Struct.__name__ = "Struct"
struct.Struct.__doc
