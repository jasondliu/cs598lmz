import _struct

class _Struct(object):
    def __init__(self, format):
        self.format = format
        self.size = _struct.calcsize(format)

    def unpack(self, data):
        return _struct.unpack(self.format, data)

    def pack(self, *values):
        return _struct.pack(self.format, *values)

S8 = _Struct('b')
U8 = _Struct('B')
S16 = _Struct('h')
U16 = _Struct('H')
S32 = _Struct('l')
U32 = _Struct('L')
S64 = _Struct('q')
U64 = _Struct('Q')
F32 = _Struct('f')
F64 = _Struct('d')

class Struct(object):
    def __init__(self, *fields):
        self.fields = fields
        self.format = ''.join([field[1] for field in fields])
        self.size = _struct.calcsize(self.format)
        self.names = [field[0]
