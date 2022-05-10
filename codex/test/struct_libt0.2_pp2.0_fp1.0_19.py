import _struct

class Struct(object):
    """
    A class that mimics the behavior of the built-in struct module, but
    uses the ctypes module to do the actual packing and unpacking.
    """
    def __init__(self, format):
        self.format = format
        self.size = _struct.calcsize(format)

    def pack(self, *values):
        return _struct.pack(self.format, *values)

    def unpack(self, data):
        return _struct.unpack(self.format, data)

    def unpack_from(self, data, offset=0):
        return _struct.unpack_from(self.format, data, offset)

# Create the Struct objects for the standard formats.

standard_formats = [
    'x', 'b', 'B', 'h', 'H', 'i', 'I', 'l', 'L', 'q', 'Q', 'f', 'd', 's', 'p', 'P'
]

