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

