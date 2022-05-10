import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield_instance():
    assert isinstance(S.x, ctypes.CField)
    assert S.x.offset == 0
    assert S.x.size == 4
    assert S.x.name == 'x'
    assert S.x.ctype == ctypes.c_int
    assert S.x.type == ctypes.c_int
    assert S.x.index == 0
    assert S.x.pack == 1
    assert S.x.bitsize == 32
    assert S.x.flags == 0
    assert S.x.type_ == 'i'
    assert S.x.alignment == 4
    assert S.x.length == 1
    assert S.x.shape == ()
    assert S.x.strides == ()
    assert S.x.subdtype is None
    assert S.x.base is None
    assert S.x.cname == 'int'
    assert S.x.__objclass__ is S
    assert S.x.__name__ == 'x'

class S2(ctypes
