import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

class A(object):
    def __init__(self):
        self.x = 1
        self.y = 2

def test_getattr():
    a = A()
    assert getattr(a, 'x') == 1
    assert getattr(a, 'y') == 2
    assert getattr(a, 'z', 3) == 3
    raises(AttributeError, getattr, a, 'z')
    raises(TypeError, getattr, a, 1)
    raises(TypeError, getattr, a, 1, 2, 3)

def test_setattr():
    a = A()
    setattr(a, 'x', 2)
    assert a.x == 2
    setattr(a, 'z', 3)
    assert a.z == 3
    raises(TypeError, setattr, a, 1, 2)
    raises(TypeError, setattr, a, 1, 2, 3)

def test_delattr():
    a = A()
    delattr(a, 'x')
