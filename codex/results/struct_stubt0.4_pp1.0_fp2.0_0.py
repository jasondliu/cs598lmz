from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')
s.unpack(b'\x01\x00\x00\x00')

# 构造一个新的结构体类型
class Struct(Struct):
    def __init__(self, format, *args):
        Struct.__init__(self, format)
        self._unpack_from = Struct.unpack_from
        self._pack_into = Struct.pack_into
        self.size = self.size + len(args)
        self.format = self.format + ' ' + ' '.join(args)
    def unpack(self, data):
        return self._unpack_from(data, 0)
    def pack(self, *args):
        return Struct.pack(self.format, *args)
    def unpack_from(self, data, offset=0):
        return self._unpack_from(data, offset)
    def pack_into(self, data, offset, *args):
        return self._pack_into(data
