import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield():
    assert ctypes.CField(ctypes.c_int, "x") == S.x

def test_cfield_attributes():
    assert S.x.name == 'x'
    assert S.x.offset == 0
    assert S.x.size == 4
    assert S.x.index == 0
    assert S.x.type is ctypes.c_int
    assert S.x.pack == 1

def test_cfield_repr():
    assert repr(S.x) == '<Field type=c_int, ofs=0, size=4>'

def test_cfield_setattr():
    raises(AttributeError, setattr, S.x, 'name', 'y')
    raises(AttributeError, setattr, S.x, 'offset', 1)
    raises(AttributeError, setattr, S.x, 'size', 2)
    raises(AttributeError, setattr, S.x, 'index', 3)
    raises(AttributeError, setattr, S.x, 'type', c
