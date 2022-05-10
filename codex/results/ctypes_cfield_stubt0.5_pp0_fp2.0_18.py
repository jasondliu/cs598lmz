import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert isinstance(S.x, ctypes.CField)
    assert S.x.offset == 0
    assert S.x.size == ctypes.sizeof(ctypes.c_int)
    assert S.x.name == 'x'
    assert S.x.type is ctypes.c_int

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int)]

def test_cfield_offset():
    assert S2.x.offset == 0
    assert S2.y.offset == ctypes.sizeof(ctypes.c_int)

class S3(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int)]
    _pack_ = 1

def test_cfield_offset_packed():
    assert S3.x.offset == 0
    assert S
