import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class MyObject(object):
    def __init__(self):
        self.x = 1
        self.y = 2
        self.z = 3

def test_from_param():
    obj = MyObject()
    p = ctypes.from_param(obj)
    assert isinstance(p, ctypes.CField)
    assert p.value == obj.x

    obj.x = 42
    assert p.value == 42

def test_from_param_invalid():
    class Foo(object):
        pass
    obj = Foo()
    raises(TypeError, ctypes.from_param, obj)

def test_from_param_invalid2():
    class Foo(object):
        _fields_ = [('x', ctypes.c_int)]
    obj = Foo()
    raises(TypeError, ctypes.from_param, obj)
