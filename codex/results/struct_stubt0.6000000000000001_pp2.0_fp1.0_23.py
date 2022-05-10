from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('d')

class Struct(object):
    def __new__(cls, format):
        return Struct.__new__(Struct)
    def __init__(self, format):
        self.format = format
    def pack(self, *args):
        return self.format.pack(*args)
    def unpack(self, *args):
        return self.format.unpack(*args)

def pack(format, *args):
    return Struct(format).pack(*args)

def unpack(format, *args):
    return Struct(format).unpack(*args)

def calcsize(format):
    return Struct(format).size

def iter_unpack(format, buffer):
    return iter(Struct(format).iter_unpack(buffer))

def pack_into(format, buffer, offset, *args):
    return Struct(format).pack_into(buffer, offset, *args)

def unpack_from(format, buffer, offset=0):
    return Struct(format).unpack_from(buffer, offset
