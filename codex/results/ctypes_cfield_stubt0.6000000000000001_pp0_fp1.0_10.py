import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
assert isinstance(S.x, ctypes.CField), repr(S.x)
assert S.x.value == 0, S.x.value
assert S.x.type == ctypes.c_int, S.x.type

assert not hasattr(S.x, 'offset')
assert not hasattr(S.x, 'size')

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

C_FIELD_TYPE = type(S.x)
assert isinstance(S.x, C_FIELD_TYPE), repr(S.x)
assert S.x.value == 0, S.x.value
assert S.x.type == ctypes.c_int, S.x.type

assert not hasattr(S.x, 'offset')
assert not hasattr(S.x, 'size')

#

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    def __init__(self, x=1):
        self
