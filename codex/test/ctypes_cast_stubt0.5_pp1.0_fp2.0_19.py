import ctypes
ctypes.cast(ctypes.pointer(ctypes.c_long(0)), ctypes.POINTER(ctypes.c_long))

# ____________________________________________________________

def test_getattr():
    class A(object):
        def __init__(self, x):
            self.x = x
    a = A(1)
    assert getattr(a, 'x') == 1
    assert getattr(a, 'y', 2) == 2
    raises(AttributeError, getattr, a, 'z')
    raises(TypeError, getattr, a, 1)
    raises(TypeError, getattr, a, 1, 2, 3)

def test_getattr_str():
    class A(object):
        def __init__(self, x):
            self.x = x
    a = A(1)
    assert getattr(a, 'x') == 1
    assert getattr(a, 'y', 2) == 2
    raises(AttributeError, getattr, a, 'z')
    raises(TypeError, getattr, a, 1)
