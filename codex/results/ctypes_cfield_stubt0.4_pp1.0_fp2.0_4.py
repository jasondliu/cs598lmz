import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class D(C):
    _fields_ = [('y', ctypes.c_int)]

class E(D):
    _fields_ = [('z', ctypes.c_int)]

def test_cfield():
    f = C.x
    assert isinstance(f, ctypes.CField)
    assert f.offset == 0
    assert f.size == 4
    assert f.index == 0
    assert f.pack == 1
    assert f.type is ctypes.c_int
    assert f.name == 'x'
    assert str(f) == '<Field type=c_int, ofs=0:4, size=4>'
    assert repr(f) == '<Field type=c_int, ofs=0:4, size=4>'

def test_cfield_parent():
    f = D.x
    assert isinstance(f, ctypes.CField)
    assert f.offset
