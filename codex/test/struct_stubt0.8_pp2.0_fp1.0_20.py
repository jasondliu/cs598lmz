from _struct import Struct
s = Struct.__new__(Struct)
s.format = '&lt;hhI'
s.size = struct.calcsize(s.format)
def unpack_from(self, buffer, offset=0):
    values = struct.unpack_from(self.format, buffer, offset)
    return values
s.unpack_from = unpack_from
s.unpack_from(data,16)
(1, 2, 3)
