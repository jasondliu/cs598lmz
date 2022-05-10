import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
assert isinstance(S.x, ctypes.CField)
assert S.x.__name__ == 'x'
assert S.x.__module__ == '__main__'
assert repr(S.x) == "<field 'x' of 'S' objects>"


class R(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    _pack_ = 2

assert R.x.offset == 2

class T(ctypes.Structure):
    _fields_ = [('x', ctypes.c_ubyte)]

assert T.x.offset == 0

class U(ctypes.Structure):
    _fields_ = [('x', ctypes.c_ubyte)]
    _pack_ = 2

assert U.x.offset == 2

class V(ctypes.Structure):
    _fields_ = [('x', ctypes.c_ubyte),
                ('y', ctypes.c_ubyte)]

assert V.x.offset == 0
assert V.y.
