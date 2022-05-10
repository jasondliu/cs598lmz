import _struct
from _struct import *
from struct import Struct

__all__ = ["Struct"]

class Struct(Struct):

    def __init__(self, format):
        self.__format = format
        self.__fmt = _struct.get_format(self.__format)
        self.__size = _struct.calcsize(self.__fmt)

    def size(self):
        return self.__size

    def pack(self, *args):
        return _struct.pack(self.__fmt, *args)

    def unpack(self, string):
        return _struct.unpack(self.__fmt, string)

    def pack_into(self, buffer, offset, *values):
        return _struct.pack_into(self.__fmt, buffer, offset, *values)

    def unpack_from(self, buffer, offset=0):
        return _struct.unpack_from(self.__fmt, buffer, offset)

    def get_format(self):
        return self.__format
