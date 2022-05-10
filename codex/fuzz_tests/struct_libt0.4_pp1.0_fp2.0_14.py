import _struct

class _Struct(object):
    """
    A class for packing and unpacking data according to a format string.

    Format strings are the same as used by the C `struct` module.
    The struct module documentation has more information.

    Methods:

    __init__() -- create a new struct object
    __len__() -- return size of the struct (in bytes)
    pack() -- convert values to bytes
    pack_into() -- convert values to bytes and write them to a buffer
    unpack() -- convert bytes to values
    unpack_from() -- convert bytes from a buffer to values
    iter_unpack() -- convert bytes to values, iteratively
    calcsize() -- return size of the struct (in bytes)

    Attributes:

    format -- the format string used by this struct
    size -- the size of the struct (in bytes)
    """

    def __init__(self, fmt):
        """Return a new Struct object which writes and reads binary data according
        to the format string fmt.
        """
        self.format = fmt
        self.size = _struct.calcsize
