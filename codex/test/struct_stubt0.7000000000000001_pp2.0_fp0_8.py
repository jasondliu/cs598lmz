from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I'
s.size = struct.calcsize(s.format)

class StructFile:
    """
    a file-like object, backed by a string buffer, that provides methods
    to read/write values according to a format string.  This is used to
    provide an interface to the file header, which has fixed locations
    for fields.
    """

    def __init__(self, buf):
        self.buf = buf
        self.offset = 0

    def __getattr__(self, attr):
        if attr in ('read', 'readline', 'readlines', 'write', 'seek',
                    'tell', 'flush', 'close', 'fileno', 'isatty',
                    'next', '__iter__',
                    '__getitem__', '__setitem__'):
            return getattr(self.buf, attr)
        raise AttributeError(attr)

