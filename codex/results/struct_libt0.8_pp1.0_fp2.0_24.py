import _struct

struct = _struct.struct
pack = _struct.pack
unpack = _struct.unpack

class Struct(object):
    def __init__(self, format):
        self.__format = format
        self.__size = struct.calcsize(format)

    def pack(self, format, value):
        return pack(format, value)

    def unpack(self, format, buffer):
        return unpack(format, buffer)

    def pack_into(self, buffer, offset, value):
        format = self.__format
        buffer[offset:offset+self.__size] = self.pack(format, value)

    def unpack_from(self, buffer, offset):
        format = self.__format
        return self.unpack(format, buffer[offset:offset+self.__size])

    @property
    def size(self):
        return self.__size


class String(object):
    @staticmethod
    def pack(format, value):
        return pack(format, value.encode('utf-8'))

    @static
