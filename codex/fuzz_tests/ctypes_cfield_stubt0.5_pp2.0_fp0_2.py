import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField(ctypes.CField):
    def __init__(self, typ, name, offset, flags):
        self.type = typ
        self.name = name
        self.offset = offset
        self.flags = flags
        self.bitsize = self.flags & 0xff

    def _get_offset(self):
        return self._offset
    def _set_offset(self, value):
        self._offset = value
        self.bitshift = value & 7
        self.bitoffset = value & ~7
    offset = property(_get_offset, _set_offset)

    def _get_bitshift(self):
        return self._bitshift
    def _set_bitshift(self, value):
        self._bitshift = value
        self.offset = self.bitoffset + value
    bitshift = property(_get_bitshift, _set_bitshift)

    def _get_bitoffset(self):
        return self._bitoffset
    def _set_bitoffset(self, value):
        self._bitoffset = value
        self.offset =
