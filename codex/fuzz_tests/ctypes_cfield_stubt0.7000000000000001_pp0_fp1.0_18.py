import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield_pickle():
    dump = pickle.dumps(S.x)
    assert pickle.loads(dump) is S.x

class X(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class Y(ctypes.Structure):
    _fields_ = [('y', ctypes.c_int)]

class Z(ctypes.Structure):
    _fields_ = [('z', ctypes.c_int)]

def test_cfield_field_name():
    assert S.x.field_name == 'x'
    assert X.x.field_name == 'x'
    assert Y.y.field_name == 'y'
    assert Z.z.field_name == 'z'


# XXX test __getattribute__
