import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
assert isinstance(S.x, ctypes.CField)

try:
    ctypes.CField = type(S.x)
except TypeError:
    pass
else:
    raise AssertionError

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

f = ctypes.CField(S2, 'x')
assert f.name == 'x'
assert f.offset == 0
assert f.size == ctypes.sizeof(ctypes.c_int)
assert f.ctype == ctypes.c_int
assert f.typecode == 'i'

f = ctypes.CField(S2, 'y')
assert f.name == 'y'
assert f.offset == ctypes.sizeof(ctypes.c_int)
assert f.size == ctypes.sizeof(ctypes.c_int)
assert f.ctype == ctypes.c_int
assert f.typecode == 'i'

#
