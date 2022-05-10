import _struct
# Test _struct.Struct class

def calcsize(fmt):
    return _struct.calcsize(fmt)

class Struct(object):

    def __init__(self, fmt):
        self.__format = fmt
        self.size = calcsize(fmt)

    def pack(self, *args):
        return _struct.pack(self.__format, *args)

    def unpack(self, s):
        return _struct.unpack(self.__format, s)

    def pack_into(self, buffer, offset, *args):
        return _struct.pack_into(self.__format, buffer, offset, *args)

    def unpack_from(self, buffer, offset=0):
        return _struct.unpack_from(self.__format, buffer, offset)

def iter_unpack(fmt, buffer):
    s = Struct(fmt)
    for i in xrange(0, len(buffer), s.size):
        yield s.unpack_from(buffer, i)

def pack_into(fmt, buffer, offset
