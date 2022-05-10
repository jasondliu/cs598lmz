from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<3s3sHH'
s.size = calcsize(s.format)

def unpack_from(buffer, offset=0):
    return s.unpack_from(buffer, offset)

def pack_into(buffer, offset, *args):
    return s.pack_into(buffer, offset, *args)

def pack(*args):
    return s.pack(*args)

def unpack(buffer):
    return s.unpack(buffer)

def calcsize():
    return s.calcsize()

class _Struct(Struct):
    def __init__(self, format, *args, **kwargs):
        self.format = format
        self.size = calcsize(format)
        super(_Struct, self).__init__(format, *args, **kwargs)

    def unpack_from(self, buffer, offset=0):
        return super(_Struct, self).unpack_from(buffer, offset)

    def pack_into(self, buffer, offset, *args):
        return super(_
