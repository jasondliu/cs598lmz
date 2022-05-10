import _struct

class Struct(object):
    def __init__(self, fmt):
        self.fmt = fmt
        self.size = _struct.calcsize(fmt)

    def pack(self, *args):
        return _struct.pack(self.fmt, *args)

    def unpack(self, str):
        return _struct.unpack(self.fmt, str)

    def unpack_from(self, str, offset=0):
        return _struct.unpack_from(self.fmt, str, offset)

class StructWithEndian(Struct):
    def __init__(self, *args, **kwargs):
        super(StructWithEndian, self).__init__(*args, **kwargs)
        self.endian = kwargs.get('endian', '<')

    def pack(self, *args):
        return _struct.pack(self.endian + self.fmt, *args)

    def unpack(self, str):
        return _struct.unpack(self.endian + self.fmt
