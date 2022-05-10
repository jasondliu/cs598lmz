import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test_cfield_subclass():
    class C(ctypes.CField):
        pass

    S._fields_ = [("y", C)]
    assert S.y.__class__ is C

def test_cfield_subclass_fails():
    class C(ctypes.CField):
        _pack_ = 1

    with raises(TypeError):
        S._fields_ = [("y", C)]

def test_cfield_subclass_fails_2():
    class C(ctypes.CField):
        _pack_ = 1

    with raises(TypeError):
        class S(ctypes.Structure):
            _fields_ = [("y", C)]

def test_cfield_subclass_fails_3():
    class C(ctypes.CField):
        _pack_ = 1

    with raises(TypeError):
        class S(ctypes.Structure):
            y = C()

def test_cfield_subclass_fails_4():
    class C(ctypes.CField):

