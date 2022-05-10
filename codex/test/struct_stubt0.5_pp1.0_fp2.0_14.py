from _struct import Struct
s = Struct.__new__(Struct)
s.size = Struct.size
s.format = Struct.format

def get_size(self):
    return self.size

def get_format(self):
    return self.format

def get_struct(self):
    return self

Struct.__getattribute__ = get_attribute
Struct.__getattr__ = get_attribute
Struct.size = property(get_size)
Struct.format = property(get_format)
Struct.struct = property(get_struct)

#-----------------------------------------------------------------------------#

class Struct(Struct):
    """A class for handling binary data."""
    def __init__(self, format):
        self.format = format
        self.size = Struct.calcsize(format)

    def unpack(self, data):
        return Struct.unpack(self.format, data)

    def pack(self, *data):
        return Struct.pack(self.format, *data)

    def __len__(self):
        return self.size

#-----------------------------------------------------------------------------#

