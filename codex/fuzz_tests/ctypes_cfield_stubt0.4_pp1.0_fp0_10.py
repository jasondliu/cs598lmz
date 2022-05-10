import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def check(f):
    assert type(f) is ctypes.CField
    assert f.name == 'x'
    assert f.type is ctypes.c_int
    assert f.offset == 0
    assert f.size == ctypes.sizeof(ctypes.c_int)
    assert f.bitsize == None
    assert f.pack == None
    assert f.index == 0

check(S.x)
check(S._fields_[0])

try:
    S.x = 1
except TypeError:
    pass
else:
    raise Exception("shouldn't be able to assign to S.x")

try:
    del S.x
except TypeError:
    pass
else:
    raise Exception("shouldn't be able to delete S.x")
