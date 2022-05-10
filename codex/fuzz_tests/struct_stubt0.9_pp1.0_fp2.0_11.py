from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>H'
s.size = 140
s.pack = _cobsr_pack
s.unpack = _cobsr_unpack
co = cobsr()

class cobsr_nz(object):  # max size = 256
    size = 256
    _format = '>H'

    def __init__(self, _x=None):
        if _x:
            self.pack(_x)

        self.unpack = self._struct.unpack
        self.pack = self._struct.pack

    def pack(self, x):
        if x:
            self.data = bytearray()
            for i in range(len(x)):
                self.data.append(x[i])
        self.data.append(0)
        if len(self.data) > self.size:
            raise ValueError('value larger than maximum limit')
        self._struct = Struct.__new__(Struct)
        self._struct.format = self._format + 'B' * len(self.data)
        self._struct
