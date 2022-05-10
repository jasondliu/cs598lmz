import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def fn(x):
    print("Function called with", x)


def test_setattr_cfield():
    fn = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

    class S(ctypes.Structure):
        _fields_ = [("foo", fn)]

    s = S()

    s.foo = fn(lambda x: x + 2)
    assert s.foo(42) == 44
    s.foo = fn(lambda x: x + 3)
    assert s.foo(42) == 45
    raises(AttributeError, setattr, s, "foo", lambda x: x + 4)


def test_setattr_structure():
    class S(ctypes.Structure):
        _fields_ = [("x", ctypes.c_int)]

    class S1(ctypes.Structure):
        _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]

    s = S(1)
    print(s.x)
    assert
