from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('l')
s.pack(1)

class Struct(object):
    def __init__(self, format):
        self.format = format
    def pack(self, *values):
        return pack(self.format, *values)
    def unpack(self, data):
        return unpack(self.format, data)

>>> s = Struct('l')
>>> s.pack(1)
b'\x01\x00\x00\x00'
>>> s.unpack(b'\x01\x00\x00\x00')
(1,)

class Struct(object):
    def __init__(self, format):
        self.format = format
        self.size = calcsize(format)
    def pack(self, *values):
        return pack(self.format, *values)
    def unpack(self, data):
        return unpack(self.format, data)
    def unpack_from(self, data, offset=0):
        return unpack_from(self.format, data,
