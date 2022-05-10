import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField(ctypes.CField):
    def __new__(self, name, type_, offset):
        self = super(CField, self).__new__(self, name, type_, offset)
        self._offset = offset
        return self

CField_p = type(S.x)
