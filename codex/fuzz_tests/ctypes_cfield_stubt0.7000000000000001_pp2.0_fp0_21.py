import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C:
    def __getitem__(self, i):
        return S.x

class E(Exception):
    pass

try:
    C()[E()]
except TypeError:
    print('TypeError')
